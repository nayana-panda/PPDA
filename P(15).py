import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('6Mcd.csv')
correlation_matrix = data.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix Heatmap')
plt.show()
