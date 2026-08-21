from dotenv import load_dotenv
import os


load_dotenv()

class Settings():
    TAVILY_API_KEY: str = os.getenv("TAVILY_API_KEY")
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY")
    AVIATIONSTACK_API_KEY: str = os.getenv("AVIATIONSTACK_API_KEY")

    # LLM models
    GEMINI_MODEL= "gemini-2.5-flash"
    GEMINI_FALLBACK_MODEL = ""
    GROQ_MODEL = "llama-3.3-70b-versatile"
    GROQ_FALLBACK_MODEL = ""

    # Threading (for database storage)
    CURRENT_THREAD_ID = "default"
    DATABASE_URL = "sqlite:///data/chatbot_memory.db"

    # Run the fastapi server
    APP_PORT = os.getenv("APP_PORT")
    APP_HOST = os.getenv("APP_HOST")

    # Flight related information
    #AVIATIONSTACK_API_KEY: str = os.getenv("AVIATIONSTACK_API_KEY")
    BASE_URL = "https://api.aviationstack.com/v1/flights"
    DEFAULT_ORIGIN_IATA = os.getenv("DEFAULT_ORIGIN_IATA", "BOM")


setting = Settings()