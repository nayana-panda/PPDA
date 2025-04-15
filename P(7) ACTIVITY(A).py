import pandas as pd

products = [
    {'product_name': 'Laptop', 'Category': 'Electronics', 'price': 3000},
    {'product_name': 'Tshirt', 'Category': 'Clothing', 'price': 1500},
    {'product_name': 'Headphone', 'Category': 'Electronics', 'price': 2500},
    {'product_name': 'Jean', 'Category': 'Clothing', 'price': 1800},
]

df = pd.DataFrame(products)
df['discounted_price'] = df['price'] * 0.90
print(df)
