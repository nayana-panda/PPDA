import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

df = pd.read_csv("4 laptops.csv")
print("original Dataframe:")
print(df.head())

enc = OneHotEncoder()
enc_data = enc.fit_transform(df[['Operating System']])
enc_df = pd.DataFrame(enc_data.toarray(),
                      columns=enc.categories_[0])
df = df.join(enc_df)
print("Data frame after one Hot Encoder 'Operating System':")
print(df.head())

le = LabelEncoder()
df['Storage'] = le.fit_transform(df[['Storage']])
print("Label Encoder classes for 'Storage' column:")
print(le.classes_)
print("Final Dataframe after Label encoding 'Storage':")
print(df.head())
