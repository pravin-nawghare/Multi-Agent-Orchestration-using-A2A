from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from config import setting
from components.prompts.final_response_prompt import FINAL_RESPONSE_PROMPT
from components.graph.state import AgentState

response_llm = setting.GEMINI_MODEL
secret_key = setting.GEMINI_API_KEY

if not secret_key:
    raise ValueError(f"Api key not provided")

response_model = ChatGoogleGenerativeAI(
    model = response_llm,
    api_key = secret_key
)

def final_response(state: AgentState):
    response_prompt = FINAL_RESPONSE_PROMPT

    response = response_model.invoke([
        SystemMessage(content="You are a professional AI travel booking assistant"),
        HumanMessage(content=response_prompt)
    ])

    print(f"final_response_agent response added in messages: {response}")

    return {
        'messages': [response],
    }