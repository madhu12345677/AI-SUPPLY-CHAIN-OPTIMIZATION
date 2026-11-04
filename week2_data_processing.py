
import pandas as pd
import json

# Load dataset
file_path = r"C:\Users\singa\Downloads\manufacture cleaned set.csv"
df = pd.read_csv(file_path)

print("WEEK 2 DATA PROCESSING")
print("---------------------")

# 1. Validate dataset
required_columns = [
    "product_id",
    "current_stock",
    "reorder_level",
    "safety_stock",
    "supplier_id",
    "supplier_rating",
    "lead_time_days",
    "daily_demand",
    "revenue_usd",
    "profit_usd"
]

missing_columns = [c for c in required_columns if c not in df.columns]

if missing_columns:
    raise ValueError(f"Missing columns: {missing_columns}")

print("Dataset validation: PASSED")
print("Total records:", len(df))

# 2. Inventory Analysis
df["stock_status"] = "Healthy"

df.loc[
    df["current_stock"] <= df["reorder_level"],
    "stock_status"
] = "Low Stock"

df.loc[
    df["current_stock"] < df["safety_stock"],
    "stock_status"
] = "Critical Stock"

# Count low stock and critical stock
low_stock = int(
    (df["current_stock"] <= df["reorder_level"]).sum()
)

critical_stock = int(
    (df["current_stock"] < df["safety_stock"]).sum()
)

# 3. Reorder Quantity Calculation
df["recommended_reorder_quantity"] = (
    df["safety_stock"]
    + df["daily_demand"] * df["lead_time_days"]
    - df["current_stock"]
).clip(lower=0)

# 4. Supplier Risk Analysis
df["supplier_risk"] = "Low"

df.loc[
    (df["supplier_rating"] < 3)
    | (df["lead_time_days"] > 45),
    "supplier_risk"
] = "High"

high_supplier_risk = int(
    (df["supplier_risk"] == "High").sum()
)

# 5. Business Metrics
results = {
    "total_records": int(len(df)),
    "low_stock_records": low_stock,
    "critical_stock_records": critical_stock,
    "high_supplier_risk_records": high_supplier_risk,
    "average_daily_demand": round(float(df["daily_demand"].mean()), 2),
    "average_supplier_rating": round(float(df["supplier_rating"].mean()), 2),
    "total_revenue": round(float(df["revenue_usd"].sum()), 2),
    "total_profit": round(float(df["profit_usd"].sum()), 2)
}

# 6. Save Results as JSON
with open("week2_business_metrics.json", "w") as file:
    json.dump(results, file, indent=4)

# 7. Display Results
print("\nBUSINESS RESULTS")
print(json.dumps(results, indent=4))

print("\nJSON file created successfully.")
