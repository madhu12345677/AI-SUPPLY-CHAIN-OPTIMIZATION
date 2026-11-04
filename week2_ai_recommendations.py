
import os
import json
from google import genai

print("WEEK 2 - AI RECOMMENDATION SYSTEM")
print("--------------------------------")

# 1. Load business metrics
with open("week2_business_metrics.json", "r") as file:
    business_data = json.load(file)

# 2. Load comparison results
with open("week2_comparison_results.json", "r") as file:
    comparison_data = json.load(file)

print("Project data loaded successfully.")

# 3. Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found.")

# 4. Connect to Gemini
client = genai.Client(api_key=api_key)

# 5. Prepare project-specific prompt
prompt = f"""
You are an AI supply chain analyst.

Analyze the following actual manufacturing dataset results.

BUSINESS METRICS:
{json.dumps(business_data, indent=2)}

STATISTICAL COMPARISONS:
{json.dumps(comparison_data, indent=2)}

Provide the following:

1. Key business insights.
2. Inventory risks and recommendations.
3. Supplier performance observations.
4. Demand forecasting observations.
5. Practical suggestions for supply chain managers.

Use simple English.
Use only the supplied data for factual claims.
Do not invent numbers.
Mention unusual metrics carefully.
"""

# 6. Generate AI recommendations
print("Connecting to Gemini AI...")

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)

# 7. Display and save response
ai_output = response.text or "No response received."

print("\nGEMINI AI RECOMMENDATIONS")
print("-------------------------")
print(ai_output)

with open(
    "week2_ai_recommendations.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write(ai_output)

print("\nAI recommendations saved successfully!")
