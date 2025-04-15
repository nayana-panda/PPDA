import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("3 salary - data.csv")
print("Original Data:")
print(df)

scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(df)
normalized_df = pd.DataFrame(normalized_data, columns=df.columns)
print("Normalized Data:")
print(normalized_df)

min_max_scaler = MinMaxScaler()
min_max_data = min_max_scaler.fit_transform(df)
min_max_df = pd.DataFrame(min_max_data, columns=df.columns)
print("MinMaxScaler:")
print(min_max_df)
