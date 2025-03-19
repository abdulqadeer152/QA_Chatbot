import os
import chainit as cl
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel(
    model_name="gemini-2-flash"
)

@cl.on_chart_start
async def handle_chart_start():
    await cl.Message(content="Hello! How can I help You Today!").send()

@cl.on_message
async def handle_message(message: cl.Message)
    
    prompt = message.content

    response = model.generate_content(prompt)