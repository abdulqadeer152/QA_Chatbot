import os
import chainlit as cl
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Ensure API key is set
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is missing. Please set it in your environment variables.")

# Configure Gemini AI
genai.configure(api_key=gemini_api_key)

# Initialize Model
model = genai.GenerativeModel(model_name="imagen-3.0-generate-002")

@cl.on_chat_start
async def handle_chat_start():
    await cl.Message(content="Hello! How can I help you today?").send()

@cl.on_message
async def handle_message(message: cl.Message):
    prompt = message.content

    # Generate response from AI model
    try:
        response = await model.generate_content_async(prompt)  # Await the async function
        response_text = response.text if hasattr(response, "text") and response.text else "I'm sorry, I couldn't generate a response."
    except Exception as e:
        response_text = f"An error occurred: {str(e)}"

    await cl.Message(content=response_text).send()

