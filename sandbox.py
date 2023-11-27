import sqlite3 as db

patient_median_information = {

# Common_information
    'age': 77.0, 'gender': 1.0, 'BMI': 26.6,
# Chronical_diseases
    'hypertensive': 0.0, 'atrialfibrillation': 0.0, 'diabetes': 0.0,
    'deficiencyanemias': 0.0, 'depression': 0.0, 'hyperlipemia': 0.0,
    'renal_failure': 0.0, 'COPD': 0.0,
# Vital_indicators
    'heart_rate': 83.0, 'EF': 55.0, 'syst_blood_press': 115.8,
    'diast_blood_press': 58.4, 'respiratory_rate': 20.3,
    'temperature': 36.6, 'SP_O2': 96.4, 'PCO2': 39.0,
    'diuresis': 1630.0,
# Laboratory_indicators
    # Red_blood
    'hematocrit': 30.8, 'RBC': 3.5, 'MCH': 29.8,
    'MCHC': 33.0, 'MCV': 90.0, 'RDW': 15.5,
    # White_blood
    'leucocyte': 9.7, 'platelets': 222.7, 'neutrophils': 80.5,
    'basophils': 0.2, 'lymphocyte': 9.2,
    # Protrombine_time, blood_coagulability
    'PT': 14.6, 'MNO': 1.3,
# Biochemistry_indicators
    'NT_proBNP': 5840.0, 'creatine_kinase': 72.7, 'creatinine': 1.3,
    'urea_nitrogen': 30.7, 'blood_Gluc': 135.6, 'blood_K': 4.1, 'blood_Na': 139.2,
    'blood_Ca': 8.5, 'blood_Cl': 102.5, 'anion_gap': 13.7, 'blood_Mg': 2.1,
    'PH': 7.4, 'bicarbonate': 26.5, 'lactic_acid': 1.4
}

con = db.connect("db.db")
cur = con.cursor()
# for item in patient_median_information.keys():
#     sql = f"""
# ALTER TABLE diagnoses ADD {item} REAL DEFAULT {patient_median_information[item]};
# """
#     cur.execute(sql)
sql = 'PRAGMA table_info(diagnoses);'
cur.execute(sql)
result = cur.fetchall()
print([i[1] for i in result[1:]])

