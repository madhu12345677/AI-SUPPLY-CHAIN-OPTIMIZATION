# Week 3 – Python Processing, Statistical Analysis and Business Insights

## 1. Project Overview

**Project Name:** AI Supply Chain & Inventory Optimization Platform

**Objective:** Process manufacturing supply chain data, perform statistical analysis, identify inventory and supplier risks, and generate actionable business insights.

**Dataset:** manufacture cleaned set.csv

- Total records: 200,000
- Total columns: 52
- Data format: CSV

## 2. Python Data Processing

Python and Pandas are used to load, process, validate, and analyze the manufacturing dataset.

Main processing steps:

1. Load the CSV dataset.
2. Validate required columns.
3. Convert numeric columns into valid numeric formats.
4. Check missing or invalid numeric values.
5. Identify duplicate records.
6. Classify inventory stock status.
7. Calculate recommended reorder quantities.
8. Identify high supplier-risk records.
9. Calculate statistical and financial metrics.
10. Generate business insights.
11. Save results as a JSON file.

## 3. Data Validation and Error Handling

The Python script includes:

- File existence validation.
- Empty dataset validation.
- Required column validation.
- Numeric value validation.
- Duplicate record checking.
- Error handling during dataset loading.
- Error handling during output file creation.
- Inventory category total verification.

**Validation Results:**

| Validation | Result |
|---|---:|
| Total records | 200,000 |
| Missing/invalid numeric values | 0 |
| Duplicate records | 0 |
| Required column validation | Passed |
| Inventory category validation | Passed |

## 4. Inventory Classification Logic

Inventory is classified using current stock, reorder level, and safety stock.

**Rules:**

- Critical Stock: current_stock < safety_stock
- Low Stock: current_stock <= reorder_level, excluding critical records in the exclusive category breakdown
- Healthy Stock: Records that meet neither condition

Critical stock receives the highest priority in the stock status classification.

**Inventory Results:**

| Inventory Metric | Records |
|---|---:|
| Total low-stock condition matches | 10,094 |
| Low stock only | 5,929 |
| Critical stock | 5,034 |
| Healthy stock | 189,037 |
| Total exclusive categories | 200,000 |

**Note:** Low-stock and critical-stock conditions can overlap. Therefore, total low-stock condition matches should not be added to the exclusive category counts.

## 5. Recommended Reorder Quantity

The system calculates a recommended reorder quantity using:

Recommended Reorder Quantity = Safety Stock + (Daily Demand × Lead Time) − Current Stock

Negative reorder quantities are set to zero.

This helps identify how much stock may be needed to support demand during supplier lead time.

## 6. Supplier Risk Analysis

Supplier risk is classified using the following rule:

- Supplier rating below 3 OR
- Lead time greater than 45 days

Records meeting either condition are classified as high risk.

**Supplier Risk Results:**

| Metric | Records |
|---|---:|
| High supplier-risk records | 149,419 |
| Low supplier-risk records | 50,581 |

Note: These are record counts, not counts of unique suppliers.

## 7. Statistical Analysis

Python calculates:

- Average daily demand
- Average actual demand
- Average forecast demand
- Difference between forecast and actual demand
- Total revenue
- Total profit
- Profit margin

**Statistical Results:**

| Metric | Result |
|---|---:|
| Average daily demand | 249.69 |
| Average actual demand | 2,750.43 |
| Average forecast demand | 9,983.55 |
| Forecast minus actual | 7,233.11 |
| Total revenue | $50,017,493,094.75 |
| Total profit | $9,001,642,610.56 |
| Profit margin | 18% |

**Profit Margin Formula:**

Profit Margin = (Total Profit / Total Revenue) × 100

## 8. Business Insights

The processing script generates simple business insights from calculated metrics.

1. 5,034 critical stock records require urgent attention.
2. 149,419 records match the high supplier-risk conditions and need further review.
3. Forecast demand is significantly higher than actual demand. Forecasting assumptions should be reviewed.
4. The calculated profit margin is 18%.

These insights can help managers prioritize inventory, review supplier performance, and investigate demand planning.

## 9. AI Feature Logic

The project uses Google's Gemini API through the Python Google GenAI SDK for AI-generated recommendations.

The Week 2 standalone AI recommendation script:

1. Reads business metrics and comparison results from JSON files.
2. Passes project-specific metrics and context into a prompt.
3. Sends the prompt to the Gemini model.
4. Receives AI-generated recommendations.
5. Saves the response in a text file.

**Model tested:** gemini-3.5-flash-lite

The Python Gemini test and recommendation scripts were executed successfully. This standalone integration is not yet confirmed as connected to the main web application.

## 10. Output Files

- `week3_processing.py` – Python processing and analysis code.
- `week3_processing_results.json` – Calculated metrics and business insights.
- `WEEK3_DOCUMENTATION.md` – Week 3 technical documentation.
- `week2_ai_recommendations.py` – Gemini AI recommendation script.
- `week2_ai_recommendations.txt` – Generated AI recommendations.
- `week2_business_metrics.json` – Business metrics.
- `week2_comparison_results.json` – Comparison results.

## 11. Conclusion

Week 3 improved the Python data processing workflow with validation, error handling, inventory classification, supplier risk analysis, statistical calculations, and automatic business insights.

The generated results provide useful information for inventory monitoring, supplier risk review, demand planning, and management decision-making.