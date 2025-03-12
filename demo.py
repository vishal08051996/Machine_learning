import os

from dotenv import load_dotenv


load_dotenv()

# Get the API key
api_key = os.getenv("GROQ_API_KEY")

# Print the key (for testing purposes)
print(f"Your API Key is: {api_key}")
# done
