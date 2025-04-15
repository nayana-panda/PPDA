import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('5ds_salaries.csv')
sns.pairplot(df)
plt.show()
