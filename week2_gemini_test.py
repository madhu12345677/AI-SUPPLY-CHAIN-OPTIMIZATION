
import os
from google import genai

try:
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("Gemini API key not found")

    client = genai.Client(api_key=api_key)

    print("Connecting to Gemini AI...")

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents="Explain supply chain management in 3 simple sentences."
    )

    print("\nGEMINI AI RESPONSE")
    print("------------------")
    print(response.text)

    print("\nGemini API integration successful!")

except Exception as error:
    print("\nGemini API test failed.")
    print("Error:", error)
