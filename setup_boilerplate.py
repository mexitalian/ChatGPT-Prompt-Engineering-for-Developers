import os
import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key  = os.getenv('OPENAI_API_KEY')
client = openai.OpenAI()

def get_completion(prompt, model="gpt-4o-mini", temperature=0):
    messages = [{"role": "user", "content": prompt}]
    response = openai.chat.completions.create(
        model=model,
        messages = [
        {
          "role": "system",
          "content": "You are a concise assistant. Always answer directly without commentary, meta references, or explanations unless explicitly asked."
        },
        {"role": "user", "content": prompt}
    ],
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message.content