import pandas as pd
import numpy as np

file_path = r"C:\Users\singa\Downloads\manufacture cleaned set.csv"
df = pd.read_csv(file_path)

print("WEEK 2 BUSINESS ANALYSIS")
print("-------------------------")

# Inventory Analysis
total_records = len(df)
low_stock = (df["current_stock"] <= df["reorder_level"]).sum()
critical_stock = (df["current_stock"] < df["safety_stock"]).sum()

print("\nINVENTORY")
print("Total Records:", total_records)
print("Low Stock Records:", low_stock)
print("Critical Stock Records:", critical_stock)

# Demand Analysis
print("\nDEMAND")
print("Average Daily Demand:", round(df["daily_demand"].mean(), 2))
print("Average Monthly Demand:", round(df["monthly_demand"].mean(), 2))
print("Average Actual Demand:", round(df["actual_demand"].mean(), 2))
print("Average Forecast Demand:", round(df["demand_forecast"].mean(), 2))

# Forecast Error
valid = df[df["actual_demand"] != 0]
mape = (np.abs(
    (valid["actual_demand"] - valid["demand_forecast"])
    / valid["actual_demand"]
).mean()) * 100

print("Forecast MAPE:", round(mape, 2), "%")

# Supplier Analysis
print("\nSUPPLIER")
print("Average Supplier Rating:", round(df["supplier_rating"].mean(), 2))
print("Average Lead Time:", round(df["lead_time_days"].mean(), 2))
print("On-Time Delivery:", round(df["on_time_delivery_rate"].mean(), 2), "%")

# Business Analysis
print("\nBUSINESS")
print("Total Revenue:", round(df["revenue_usd"].sum(), 2))
print("Total Profit:", round(df["profit_usd"].sum(), 2))
print("Average Shipping Cost:", round(df["shipping_cost_usd"].mean(), 2))
print("Supply Chain Efficiency:", round(df["supply_chain_efficiency"].mean(), 2))
print("Sustainability Score:", round(df["sustainability_score"].mean(), 2))