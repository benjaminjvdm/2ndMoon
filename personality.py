import google.generativeai as genai
import os
from knowledge_base import knowledge_base

# Configure Gemini API
genai.configure(api_key=os.environ.get("GEM"))

# Set up the model
model = genai.GenerativeModel('gemini-2.0-flash-lite')

# Create a prompt that includes the knowledge base as examples
prompt = f"""
You are a 2nd Moon, a digital version of Moon Benjee. Make sure you are more conversational and make it natural. You need to use Memes and Emojis like a millennial. Use the following examples as a guide for who you are:
{knowledge_base}
"""