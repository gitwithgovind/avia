"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""
from dotenv import load_dotenv
import os
import google.generativeai as genai




load_dotenv()  # take environment variables from .env.
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content(
    'Tell me a story about a magic backpack.',
    generation_config=genai.types.GenerationConfig(
        # Only one candidate for now.
        candidate_count=1,
        stop_sequences=['x'],
        max_output_tokens=200,
        temperature=1.0)
)

text = response.text

if response.candidates[0].finish_reason.name == "MAX_TOKENS":
    text += '...'

print(text)