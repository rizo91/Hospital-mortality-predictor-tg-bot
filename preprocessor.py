
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer

def data_reader(file_name):
    data = pd.read_csv(file_name).copy()
    df = data.drop(columns=['ID', 'survive'])
    return df


def data_preprocessing(data_frame):
    num_features = data_frame.columns

    transformer = make_pipeline(
        SimpleImputer(strategy='constant'),  # possible: 'most_frequents' and 'mean'.
        StandardScaler(),  # Standartize our data.
    )
    preprocessor = make_column_transformer(
        (transformer, num_features)
    )

    return preprocessor






