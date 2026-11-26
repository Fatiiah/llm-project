from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")


client = genai.Client()


SYSTEM_PROMPT = '''
You are a learning assistant.
Explain concepts clearly and simply.
use examples when useful.
if you are unsure, say you are unsure.

if user asks any question related to mathematics, you should reply with "I am not able to answer questions related to mathematics"
'''

def get_response(prompt):
    interaction = client.interactions.create(
        model="gemini-3.5-flash-lite",
        system_instruction = SYSTEM_PROMPT,
        input=prompt,
    )
    print(interaction.output_text)

input_prompt = input("Ask a question:")
get_response(input_prompt)

