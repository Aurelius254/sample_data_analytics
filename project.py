# Supermarket dataset deep analysis
import pandas as pd
df = pd.read_csv("SampleSuperstore.csv")

# To preview the first few rows
df.drop(columns = ["Postal Code"], inplace = True)
df.info()
df.describe()
print()

# Getting insights from data

# Sub-Category By number of sales
top_sales = df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending = False).head(10)
print(top_sales)
print()

# Sub-Category By Profit
profit_by_category = df.groupby("Sub-Category")["Profit"].sum().sort_values(ascending = False)
print(profit_by_category)
print()

# Sub-Category By Average Discount
avg_discount = df.groupby("Sub-Category")["Discount"].mean().sort_values(ascending = False)
print(avg_discount)
print()

# Profit by State
state_profit = df.groupby("State")[["Sales","Profit"]].sum().sort_values(by = "Profit", ascending = False)
print(state_profit.head(10))
print()

# Deep Dive on Texas
texas_data = df[df["State"] == "Texas"]
texas_data.head()

# Check Sales vs Profit by Sub-Category
texas_summary = texas_data.groupby("Sub-Category")[["Sales", "Profit"]].sum().sort_values(by = "Profit")
print(texas_summary)
print()

# Average Discount by sub_category
discounts_texas = texas_data.groupby("Sub-Category")["Discount"].mean().sort_values(ascending=False)
print(discounts_texas)
print()

# Deep Dive on California
california_data = df[df["State"] == "California"]
california_data.head()

# Check Sales vs Profit by Sub-Category
california_summary = california_data.groupby("Sub-Category")[["Sales", "Profit"]].sum().sort_values(by = "Profit")
print(california_summary)
print()

# Average Discount by sub_category
discounts_california = california_data.groupby("Sub-Category")["Discount"].mean().sort_values(ascending=False)
print(discounts_california)
print()

# Exporting cleaned data
df.to_csv("cleaned_SampleSuperstore.csv", index = False)
texas_data.to_csv("cleanedtexas_data.csv", index = False)
