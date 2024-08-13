import pandas as pd


def get_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df
