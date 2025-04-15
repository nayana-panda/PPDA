import pandas as pd

# Replace 'experience_data.csv' with the path to your CSV file
file_path = 'experience_data.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# 1. Display the last 3 rows
print("Last 3 rows of the dataset:")
print(df.tail(3))

# 2. Display description and information of the DataFrame
print("\nDescription of the DataFrame:")
print(df.describe(include='all'))  # include='all' to get non-numeric columns too

print("\nInformation about the DataFrame:")
print(df.info())

# 3. Display column names
print("\nColumn names:")
print(df.columns.tolist())

