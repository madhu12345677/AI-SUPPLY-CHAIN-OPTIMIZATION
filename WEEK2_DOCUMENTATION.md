

\# Week 2 – Python Business Logic and Generative AI Integration



\## 1. Project Overview

Project Name: AI Supply Chain and Inventory Optimization Platform



Objective:

To analyze manufacturing data using Python, calculate important business metrics, compare operational performance, and generate AI-based recommendations using the Gemini API.



\## 2. Dataset Processing

\- Dataset: Manufacturing cleaned dataset

\- Total Records: 200,000

\- Total Columns: 52

\- Tool: Python

\- Libraries: Pandas, JSON, Google GenAI



Dataset validation and required-column checks were implemented.



\## 3. Python Business Calculations



Implemented in:

\- week2\_business\_analysis.py

\- week2\_data\_processing.py



Calculated:

\- Total inventory records

\- Low stock records

\- Critical stock records

\- Supplier risk records

\- Average daily demand

\- Average supplier rating

\- Total revenue

\- Total profit



\### Business Results



| Metric | Result |

|---|---:|

| Total Records | 200,000 |

| Low Stock Records | 10,094 |

| Critical Stock Records | 5,034 |

| High Supplier Risk Records | 149,419 |

| Average Daily Demand | 249.69 |

| Average Supplier Rating | 3.00 |

| Total Revenue | $50,017,493,094.75 |

| Total Profit | $9,001,642,610.56 |



\## 4. Statistical Comparisons



Implemented in:

\- week2\_comparisons.py



Comparisons include:

\- Actual demand vs forecast demand

\- Supplier rating and lead time

\- On-time delivery rate

\- Low stock vs critical stock

\- Revenue vs profit



\### Important Observations

\- Average actual demand: 2,750.43

\- Average forecast demand: 9,983.55

\- Forecast exceeds actual demand by 7,233.11 on average.

\- Average supplier lead time: 44.99 days.

\- Average on-time delivery rate: 49.97%.

\- Profit margin: 18.00%.



\## 5. Generative AI Integration



Implemented using:

\- week2\_gemini\_test.py

\- week2\_ai\_recommendations.py



Technology:

\- Google Gemini API

\- Python Google GenAI SDK

\- Model: gemini-3.5-flash-lite



The Gemini API connection was tested successfully.



Actual business metrics and statistical comparison results were loaded from JSON files and sent to Gemini through a project-specific prompt.



Gemini generated recommendations related to:

\- Inventory optimization

\- Supplier risk management

\- Demand forecasting

\- Business performance

\- Operational improvements



Generated AI output is saved in:

\- week2\_ai\_recommendations.txt



\## 6. Output Files



\- week2\_business\_metrics.json

\- week2\_comparison\_results.json

\- week2\_ai\_recommendations.txt



\## 7. Testing and Validation



\- Dataset loading: Successful

\- Dataset validation: Passed

\- Business calculations: Executed successfully

\- Statistical comparisons: Executed successfully

\- Gemini API connection: Successful

\- AI recommendation generation: Successful

\- AI output file creation: Successful



\## 8. Conclusion



Week 2 implemented Python-based data processing, business calculations, statistical comparisons, and Generative AI integration.



The system uses actual manufacturing dataset results to generate AI-based supply chain recommendations through the Gemini API.



