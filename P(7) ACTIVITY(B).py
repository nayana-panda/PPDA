import numpy as np
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'np.nan'],
    'Age': [25, np.nan, 30, 22, 28],
    'Salary': [50000, 60000, np.nan, 55000, 120000]
}

df = pd.DataFrame(data)
print("Original Dataframe")
print(df)

df.fillna(method='ffill', inplace=True)
df.drop_duplicates(inplace=True)

print("\nDataframe after handling missing values and duplicates")
print(df)
