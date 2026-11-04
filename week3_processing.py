
import pandas as pd
import json
import os

print("WEEK 3 - ADVANCED DATA PROCESSING")
print("--------------------------------")

# 1. Load dataset safely
file_path = r"C:\Users\singa\Downloads\manufacture cleaned set.csv"

try:
    if not os.path.exists(file_path):
        raise FileNotFoundError("Dataset file not found. Check the file path.")

    df = pd.read_csv(file_path)

    if df.empty:
        raise ValueError("Dataset is empty.")

    print("Dataset loaded successfully.")

except Exception as error:
    print("Dataset loading failed:", error)
    raise SystemExit

# 2. Validate required columns
required_columns = [
    "product_id",
    "current_stock",
    "reorder_level",
    "safety_stock",
    "supplier_rating",
    "lead_time_days",
    "daily_demand",
    "actual_demand",
    "demand_forecast",
    "revenue_usd",
    "profit_usd"
]

missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

if missing_columns:
    print("Missing columns:", missing_columns)
    raise SystemExit("Dataset validation failed.")

print("Required column validation: PASSED")

# 3. Convert numeric columns safely
numeric_columns = [
    "current_stock",
    "reorder_level",
    "safety_stock",
    "supplier_rating",
    "lead_time_days",
    "daily_demand",
    "actual_demand",
    "demand_forecast",
    "revenue_usd",
    "profit_usd"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

invalid_values = int(df[numeric_columns].isna().sum().sum())

print("Invalid or missing numeric values:", invalid_values)

if invalid_values > 0:
    raise SystemExit(
        "Validation failed: Fix invalid or missing numeric values."
    )

# 4. Check duplicate records
duplicate_records = int(df.duplicated().sum())

print("Duplicate records:", duplicate_records)

# 5. Inventory classification
df["stock_status"] = "Healthy"

# Total low stock includes critical stock
df.loc[
    df["current_stock"] <= df["reorder_level"],
    "stock_status"
] = "Low Stock"

# Critical stock is a subset of total low stock
df.loc[
    df["current_stock"] < df["safety_stock"],
    "stock_status"
] = "Critical Stock"

total_low_stock = int(
    (df["current_stock"] <= df["reorder_level"]).sum()
)

critical_stock = int(
    (df["current_stock"] < df["safety_stock"]).sum()
)

low_stock_only = total_low_stock - critical_stock

healthy_stock = int(
    (df["stock_status"] == "Healthy").sum()
)

print("Total low stock (including critical):", total_low_stock)
print("Low stock only:", low_stock_only)
print("Critical stock:", critical_stock)
print("Healthy stock:", healthy_stock)

# 6. Recommended reorder quantity
df["recommended_reorder_quantity"] = (
    df["safety_stock"]
    + df["daily_demand"] * df["lead_time_days"]
    - df["current_stock"]
).clip(lower=0)

# 7. Supplier risk analysis
df["supplier_risk"] = "Low"

df.loc[
    (df["supplier_rating"] < 3)
    | (df["lead_time_days"] > 45),
    "supplier_risk"
] = "High"

high_supplier_risk = int(
    (df["supplier_risk"] == "High").sum()
)

# 8. Statistical analysis
average_daily_demand = float(df["daily_demand"].mean())
average_actual_demand = float(df["actual_demand"].mean())
average_forecast_demand = float(df["demand_forecast"].mean())

demand_difference = (
    average_forecast_demand - average_actual_demand
)

total_revenue = float(df["revenue_usd"].sum())
total_profit = float(df["profit_usd"].sum())

profit_margin = (
    total_profit / total_revenue * 100
    if total_revenue != 0 else 0
)

# 9. Business insights
business_insights = []

if critical_stock > 0:
    business_insights.append(
        f"Urgent attention required for {critical_stock} critical stock records."
    )

if high_supplier_risk > 0:
    business_insights.append(
        f"Review {high_supplier_risk} high supplier-risk records."
    )

if demand_difference > 0:
    business_insights.append(
        "Forecast demand is higher than actual demand. Review forecasting assumptions."
    )
elif demand_difference < 0:
    business_insights.append(
        "Actual demand is higher than forecast demand. Review demand planning."
    )
else:
    business_insights.append(
        "Average forecast demand matches average actual demand."
    )

business_insights.append(
    f"Calculated profit margin is {profit_margin:.2f}%."
)

# 10. Prepare results
results = {
    "total_records": int(len(df)),
    "duplicate_records": duplicate_records,
    "invalid_numeric_values": invalid_values,
    "total_low_stock_records": total_low_stock,
    "low_stock_only_records": low_stock_only,
    "critical_stock_records": critical_stock,
    "healthy_stock_records": healthy_stock,
    "high_supplier_risk_records": high_supplier_risk,
    "average_daily_demand": round(average_daily_demand, 2),
    "average_actual_demand": round(average_actual_demand, 2),
    "average_forecast_demand": round(average_forecast_demand, 2),
    "forecast_minus_actual": round(demand_difference, 2),
    "total_revenue": round(total_revenue, 2),
    "total_profit": round(total_profit, 2),
    "profit_margin_percent": round(profit_margin, 2),
    "business_insights": business_insights
}

# 11. Save JSON output
try:
    with open(
        "week3_processing_results.json",
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(results, file, indent=4)

    print("\nResults saved to week3_processing_results.json")

except OSError as error:
    print("Could not save results:", error)
    raise SystemExit

# 12. Display final output
print("\nWEEK 3 PROCESSING RESULTS")
print("-------------------------")
print(json.dumps(results, indent=4))

print("\nWEEK 3 BUSINESS INSIGHTS")
print("-----------------------")

for insight in business_insights:
    print("-", insight)

print("\nWeek 3 processing completed successfully!")
