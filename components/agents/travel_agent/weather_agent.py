from langchain_google_genai import ChatGoogleGenerativeAI
from config import setting


weather_llm = setting.GEMINI_MODEL
secret_key = setting.GEMINI_API_KEY

if not secret_key:
    raise ValueError(f"Api key not provided")

weather_model = ChatGoogleGenerativeAI(
    model = weather_llm,
    api_key = secret_key
)