import markdown
from config import setting
from components.graph.state import AgentState
from components.prompts.destination_prompt import extraction_prompt
from langchain_google_genai import ChatGoogleGenerativeAI

destination_api_key = setting.GEMINI_API_KEY
destination_model = setting.GEMINI_MODEL

if not destination_api_key:
    raise ValueError(f"Api key not provided")

destination_extract_model = ChatGoogleGenerativeAI(
    model = destination_model,
    api_key = destination_api_key
)

def extract_destination(state: AgentState):

    destination_prompt = extraction_prompt.format_prompt(
        user_query = state.get("user_query", "")
    )
    destination = destination_extract_model.invoke(destination_prompt)
    return destination.content.strip()

def load_email_body(source, is_file=True):
    """
    Load Markdown content from a file or use content directly.

    Args:
        source: File path or Markdown content.
        is_file: True if source is a file path,
                 False if source is Markdown content.

    Returns:
        Markdown content as a string.
    """

    if is_file:
        with open(source, "r", encoding="utf-8") as file:
            return file.read()

    return source

def markdown_to_html(source, is_file=False):
    """
    Convert Markdown content or a Markdown file to HTML.

    Args:
        source: Markdown content or file path.
        is_file: True if source is a file path,
                 False if source is Markdown content.

    Returns:
        HTML content as a string.
    """

    markdown_content = load_email_body(
        source,
        is_file=is_file
    )

    return markdown.markdown(
        markdown_content,
        extensions=["extra"]
    )