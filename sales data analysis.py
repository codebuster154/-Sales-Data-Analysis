import pandas as pd

#Load Data
# Using r'' to avoid path errors if you use the full path
try:
    df = pd.read_csv(r'C:\Users\ssand\Desktop\datascience\Tasks\task 3\sales_data.csv')
except FileNotFoundError:
    print("Error: 'sales_data.csv' not found. Please check the file path.")

# Clean Data
# Fill missing 'Total_Sales' with 0 and remove any duplicate rows
df['Total_Sales'] = df['Total_Sales'].fillna(0)
df = df.drop_duplicates()

#(3 Metrics)

# Metric 1: Total Revenue
total_revenue = df['Total_Sales'].sum()

# Metric 2: Best-Selling Product
# Group by Product and sum the quantities
best_product = df.groupby('Product')['Quantity'].sum().idxmax()
units_sold = df.groupby('Product')['Quantity'].sum().max()

# Metric 3: Average Order Value (AOV)
avg_order = df['Total_Sales'].mean()

# --- DAY 5: Create Formatted Report ---
print("-" * 30)
print("SALES PERFORMANCE REPORT")
print("-" * 30)
print(f"Total Revenue:      ₹{total_revenue:,.2f}")
print(f"Average Order:      ₹{avg_order:,.2f}")
print(f"Best Seller:        {best_product} ({units_sold} units)")
print("-" * 30)