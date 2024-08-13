from data.settings.config import DF_PATH
from shared.data import get_data

df = get_data(DF_PATH)

print(df.head())

print(df["sepal_length"].agg(["mean", "std", "count"]))

print(df.describe())
