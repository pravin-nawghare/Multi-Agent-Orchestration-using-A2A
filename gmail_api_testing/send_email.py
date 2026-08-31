# this file sends email via Gmail API
import base64
import os.path
from email.message import EmailMessage
import markdown
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/gmail.send"]


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



def get_gmail_service():
    creds = None

    # Load previously saved credentials
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file(
            "token.json",
            SCOPES
        )

    # If credentials don't exist or aren't valid, authenticate
    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "client_secret.json",
                SCOPES
            )

            creds = flow.run_local_server(port=0)

        # Save credentials for next time
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return build("gmail", "v1", credentials=creds)


def send_email():
    try:
        service = get_gmail_service()

        message = EmailMessage()

        markdown_content = load_email_body(
            "README.md",
            is_file=True
)

        html_content = markdown_to_html(
            "README.md",
            is_file=True
        )

# If directly text is passing to the function
# markdown_content = load_email_body(
#     "# Hello\n\nThis is **important**.",
#     is_file=False
# )

# html_content = markdown_to_html(
#     "# Hello\n\nThis is **important**.",
#     is_file=False
# )

        message.set_content(
            markdown_content
        )

        # Add HTML version
        message.add_alternative(
            html_content,
            subtype="html"
        )

        recipents = [
            # add email id of different all users to want to sent email with comma
        ]

        # message["To"] = ', '.join(recipents)
        message["To"] = "pruthanawghare@gmail.com"
        message["Subject"] = "Automated email"

        encoded_message = base64.urlsafe_b64encode(
            message.as_bytes()
        ).decode()

        # when passing content directly here use this
        # create_message = {
        #     "raw": encoded_message
        # }

        send_message = (
            service.users()
            .messages()
            .send(
                userId="me",
                body={"raw": encoded_message}#create_message
            )
            .execute()
        )

        print(
            f'Email sent successfully. '
            f'Message ID: {send_message["id"]}'
        )

    except HttpError as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    send_email()