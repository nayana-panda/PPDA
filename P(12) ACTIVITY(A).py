import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("4 laptops.csv")
df2 = pd.read_csv("screen_size.csv")

plt.boxplot(df['Screen Size - inches'])
plt.xlabel("Screen Size - inches")
plt.ylabel("values")
plt.title("Boxplot of Screen Size")
plt.show()

plt.boxplot([df['Weight - kg'], df['Price - INR']])
plt.xlabel("Weight - kg, Price - INR")
plt.ylabel("values")
plt.title("Boxplot of Weight and Price")
plt.show()

plt.boxplot(df['RAM Size - GB'])
plt.xlabel("RAM Size - GB")
plt.ylabel("values")
plt.title("Boxplot of RAM Size")
plt.show()

import seaborn as sns
sns.boxplot(df2['weight-kg'])
plt.show()
sns.boxplot(df2['Screen-Size-inches'])
plt.show()
sns.boxplot(df2['price'])
plt.show()
sns.boxplot(x=df2['weight-kg'], y=df2['RAM'])
plt.show()
sns.boxplot(x=df2['Screen-Size-inches'], y=df2['RAM'])
plt.show()
sns.boxplot(x=df2['price'], y=df2['RAM'])
plt.show()
