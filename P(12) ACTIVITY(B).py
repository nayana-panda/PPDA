import pandas as pd

data = pd.read_csv("4 laptops.csv")

q1 = data['Screen Size - inches'].quantile(0.25)
q3 = data['Screen Size - inches'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = data[(data['Screen Size - inches'] < lower_bound) | (data['Screen Size - inches'] > upper_bound)]

print("Lower bound =", lower_bound)
print("Upper bound =", upper_bound)
print("Outliers are:")
print(outliers)
print("No of outliers:", outliers.shape[0])
