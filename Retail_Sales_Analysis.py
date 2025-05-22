import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r'C:\Users\ajink\Downloads\Superstore.csv', encoding='ISO-8859-1')

# Display basic info
print(df.shape)
df.head()

# Drop duplicates
df.drop_duplicates(inplace=True)

# Convert 'Order Date' and 'Ship Date' to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Check for missing values
print(df.isnull().sum())

# Optional: fill or drop missing values if any

# Total Sales by Category

category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
sns.barplot(x=category_sales.index, y=category_sales.values, palette='pastel')
plt.title('Total Sales by Category')
plt.ylabel('Sales')
plt.show()

# Top 10 selling products

top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(y=top_products.index, x=top_products.values, palette='viridis')
plt.title('Top 10 Best-Selling Products')
plt.xlabel('Sales')
plt.ylabel('Product Name')
plt.show()

# Monthly Sales Trend

df['Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()

monthly_sales.plot(kind='line', figsize=(12, 6), marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()


# Profit by Region

region_profit = df.groupby('Region')['Profit'].sum()

plt.figure(figsize=(8, 5))
sns.barplot(x=region_profit.index, y=region_profit.values, palette='coolwarm')
plt.title('Profit by Region')
plt.ylabel('Profit')
plt.show()


# Sales vs. Profit Scatter Plot

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Sales', y='Profit', hue='Category', alpha=0.6)
plt.title('Sales vs Profit by Category')
plt.show()

