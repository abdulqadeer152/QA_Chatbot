import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model =genai.GenerativeModel(model_name="gemini-2-flash")

response = model.generate_content("Teach me about how an LLM Works?")

print(response.text)  