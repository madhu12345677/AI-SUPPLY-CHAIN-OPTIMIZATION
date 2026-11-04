

\# Week 2 – Technical Implementation Details



\## 1. Project Overview



Project: AI Supply Chain and Inventory Optimization Platform



Objective:

Process manufacturing data using Python, calculate inventory and supplier performance metrics, compare business performance, and generate AI-based recommendations using Google Gemini API.



Dataset:

\- File: manufacture cleaned set.csv

\- Records: 200,000

\- Columns: 52



\## 2. Python Implementation



The following Python scripts were developed and executed.



| Script | Implementation |

|---|---|

| week2\_business\_analysis.py | Calculates inventory, demand, supplier and business metrics |

| week2\_data\_processing.py | Validates data, classifies stock status and calculates reorder quantity |

| week2\_comparisons.py | Compares actual demand, forecast demand, supplier performance and financial metrics |

| week2\_gemini\_test.py | Tests Gemini API connectivity |

| week2\_ai\_recommendations.py | Sends actual project metrics to Gemini and generates recommendations |



Libraries:

\- pandas – Data processing

\- json – Reading and saving structured results

\- google-genai – Gemini API integration

\- os – Reading API key from environment variables



\## 3. Business Logic and Formulas



\### A. Inventory Classification



Low Stock:

current\_stock <= reorder\_level



Critical Stock:

current\_stock < safety\_stock



Healthy:

Initial default classification before applying the stock rules.



Python implementation:



```python

df\["stock\_status"] = "Healthy"



df.loc\[

&#x20;   df\["current\_stock"] <= df\["reorder\_level"],

&#x20;   "stock\_status"

] = "Low Stock"



df.loc\[

&#x20;   df\["current\_stock"] < df\["safety\_stock"],

&#x20;   "stock\_status"

] = "Critical Stock"

```



The critical stock condition is applied after the low-stock condition and therefore overrides the label when both conditions apply.



\### B. Recommended Reorder Quantity



Formula:



Recommended Reorder Quantity =

Safety Stock + (Daily Demand × Lead Time) - Current Stock



Negative results are converted to zero.



Python implementation:



```python

df\["recommended\_reorder\_quantity"] = (

&#x20;   df\["safety\_stock"]

&#x20;   + df\["daily\_demand"] \* df\["lead\_time\_days"]

&#x20;   - df\["current\_stock"]

).clip(lower=0)

```



\### C. Supplier Risk



A record is classified as High Risk if:



\- Supplier rating < 3, OR

\- Lead time > 45 days



Python implementation:



```python

df\["supplier\_risk"] = "Low"



df.loc\[

&#x20;   (df\["supplier\_rating"] < 3)

&#x20;   | (df\["lead\_time\_days"] > 45),

&#x20;   "supplier\_risk"

] = "High"

```



Note: These are record-level classifications, not unique supplier counts.



\### D. Financial Metrics



Total Revenue = Sum of revenue\_usd



Total Profit = Sum of profit\_usd



Profit Margin =

(Total Profit / Total Revenue) × 100



\### E. Demand Comparison



Demand Difference =

Average Forecast Demand - Average Actual Demand



\## 4. Business Calculation Results



| Metric | Result |

|---|---:|

| Total records | 200,000 |

| Low stock records | 10,094 |

| Critical stock records | 5,034 |

| High supplier risk records | 149,419 |

| Average daily demand | 249.69 |

| Average supplier rating | 3.00 |

| Average lead time | 44.99 days |

| On-time delivery rate | 49.97% |

| Total revenue | $50,017,493,094.75 |

| Total profit | $9,001,642,610.56 |



\## 5. Gemini API Integration



Provider: Google Gemini API



Python SDK: google-genai



Model: gemini-3.5-flash-lite



API key management:

The API key is stored in the GEMINI\_API\_KEY environment variable. It is not hardcoded in the source code.



\### API Integration Code



```python

import os

from google import genai



api\_key = os.getenv("GEMINI\_API\_KEY")



client = genai.Client(api\_key=api\_key)



response = client.models.generate\_content(

&#x20;   model="gemini-3.5-flash-lite",

&#x20;   contents=prompt

)



print(response.text)

```



Generation configuration:

No custom temperature, token limit or other generation settings were specified. The model's default settings were used.



\### Actual Prompt Template



```text

You are an AI supply chain analyst.



Analyze the following actual manufacturing dataset results.



BUSINESS METRICS:

\[Business metrics loaded from week2\_business\_metrics.json]



STATISTICAL COMPARISONS:

\[Comparison results loaded from week2\_comparison\_results.json]



Provide the following:



1\. Key business insights.

2\. Inventory risks and recommendations.

3\. Supplier performance observations.

4\. Demand forecasting observations.

5\. Practical suggestions for supply chain managers.



Use simple English.

Use only the supplied data for factual claims.

Do not invent numbers.

Mention unusual metrics carefully.

```



The actual Python program dynamically inserts JSON data into the prompt.



\## 6. Sample AI Input



Input files:

\- week2\_business\_metrics.json

\- week2\_comparison\_results.json



Example input values:



```json

{

&#x20; "total\_records": 200000,

&#x20; "low\_stock\_records": 10094,

&#x20; "critical\_stock\_records": 5034,

&#x20; "high\_supplier\_risk\_records": 149419,

&#x20; "average\_daily\_demand": 249.69,

&#x20; "average\_supplier\_rating": 3.0,

&#x20; "total\_revenue": 50017493094.75,

&#x20; "total\_profit": 9001642610.56

}

```



\## 7. Sample Gemini Output



The Gemini API connection and recommendation generation were successfully tested.



Actual generated recommendations included:



\- Prioritize 5,034 critical-stock records.

\- Investigate the 149,419 high supplier-risk records.

\- Review supplier performance because average on-time delivery is 49.97%.

\- Investigate the large gap between forecast demand (9,983.55) and actual demand (2,750.43).

\- Improve demand planning and supplier reliability.



Full generated response is saved in:

week2\_ai\_recommendations.txt



\## 8. Testing Evidence



| Test | Result |

|---|---|

| Dataset loading | Successful |

| Dataset validation | Passed |

| Business calculations | Successful |

| Statistical comparisons | Successful |

| Gemini API connection | Successful |

| Gemini response generation | Successful |

| AI output saved to text file | Successful |



\## 9. How the Logic Can Be Consumed by an App/API



The current implementation runs as standalone Python scripts.



A future API integration can follow this workflow:



1\. The app sends a request to a Python API endpoint.

2\. The API loads or receives manufacturing data.

3\. Python processing functions calculate inventory and supplier metrics.

4\. The API returns structured JSON results to the app.

5\. An AI endpoint sends the calculated metrics to Gemini.

6\. Gemini returns recommendations.

7\. The app displays the metrics and recommendations on its dashboard.



Suggested API endpoints:

\- GET /api/business-metrics

\- GET /api/inventory-analysis

\- GET /api/supplier-risk

\- POST /api/ai-recommendations



These endpoints are proposed integration points; they have not yet been implemented or tested.



\## 10. Conclusion



Week 2 implemented and tested Python data processing, inventory and supplier business logic, statistical comparisons, and Google Gemini API-based recommendations.



The implementation uses actual manufacturing dataset results and saves generated AI recommendations for further use in the supply chain application.



