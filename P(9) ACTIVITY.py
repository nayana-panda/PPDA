import pandas as pd
df = vd.read_csv('2 Salary.csv')

Description = df['2 Salary'].describe()

Quantiles = df['2 Salary'].quantile([0.25, 0.5, 0.75])

Skewness = df['2 Salary'].skew()

Kurtosis = df['2 Salary'].kurt()

Value_counts = df['2 Salary'].value_counts()

print("Statistical Summary:".description)
print("Skewness:", Skewness)
print("Kurtosis:", Kurtosis)
print("Value Counts:", Value Counts)
