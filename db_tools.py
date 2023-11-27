import sqlite3 as db
import json

from functools import wraps
from threading import Lock

lock = Lock()


def db_query(db_function):
    @wraps(db_function)
    def wrapper(*args, **kwargs):
        global lock
        con = db.connect("db.db")
        cur = con.cursor()
        try:
            sql = db_function(*args, **kwargs)
            lock.acquire(True)
            cur.execute(sql)
            lock.release()
        except db.DatabaseError as err:
            pass

        else:
            con.commit()
            lock.acquire(True)
            result = cur.fetchall()
            lock.release()
            return [list(row) for row in result]
        con.close()
    return wrapper


def result_simplifier(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        if len(result) == 1 and str(type(result[0])) == "<class 'list'>":
            result = result[0][0]
        else:
            result = [i[0] for i in result]
        return result
    return wrapper


@db_query
def insert_values(table, columns, values):
    # if type(values) == str:
    #     values = values.replace('\'', '`')
    sql = f"""
INSERT OR REPLACE INTO {table} ({columns}) VALUES ({values});
"""
    return sql


@db_query
def set_value(table, column, value, criteria='1=1'):
    # if type(value) == str:
    #     value = value.replace('\'', '`')
    sql = f"""
UPDATE {table} SET {column}={value} WHERE {criteria};
"""
    return sql


@db_query
def delete_rows(table, criteria='1=1'):
    sql = f"""
DELETE FROM {table} WHERE {criteria};
"""
    return sql


@result_simplifier
@db_query
def fetch_column(table, column, criteria='1=1', order='1'):
    sql = f"""
SELECT {column} FROM {table} WHERE {criteria} ORDER BY {order};
"""
    return sql


@db_query
def fetch_data(table, column, criteria='1=1', order='1'):
    sql = f"""
SELECT {column} FROM {table} WHERE {criteria} ORDER BY {order};
"""
    return sql


def fetch_list(table, column='*', criteria='1=1', order='1'):
    query_data = fetch_data(table, column, criteria, order)
    result = []
    if len(query_data) == 1 and type(query_data[0]) == list:
        result = [i for i in query_data[0]]
    elif len(query_data) > 1:
        result = [i[0] for i in query_data]
    return result


def diagnosis_columns():
    con = db.connect("db.db")
    cur = con.cursor()
    sql = 'PRAGMA table_info(diagnoses);'
    cur.execute(sql)
    result = cur.fetchall()
    return [i[1] for i in result[1:]]


with open('data.json', encoding='utf-8') as file:
    DIAGNOSIS_DATA = json.load(file)
