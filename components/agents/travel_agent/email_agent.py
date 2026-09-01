# this file sends email via Gmail API
import base64
import os.path
from email.message import EmailMessage
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from components.utils import load_email_body, markdown_to_html
from config import setting

email_scope = setting.EMAIL_SCOPE
SCOPES = [email_scope]


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
            # nawgharepravin0@gmail.com,
            # piratehuntrer@gmail.com
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