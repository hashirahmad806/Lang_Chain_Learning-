from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import warnings

warnings.filterwarnings("ignore")
load_dotenv()

api_key = os.getenv("Google_Gemini_API_KEY")

model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    api_key=api_key
    ,temperature=0.7
)

answer = model.invoke(
    "Write a poem about the beauty of nature."
)

print(answer.content[0]["text"])
