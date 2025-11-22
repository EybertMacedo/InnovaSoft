import os.path
import base64
import json
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

def get_gmail_service():
    creds = None
    # Try loading token from file first, then environment variable
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    else:
        # Check for TOKEN_JSON (user preferred) or GOOGLE_TOKEN_JSON (fallback)
        token_json = os.getenv("TOKEN_JSON") or os.getenv("GOOGLE_TOKEN_JSON")
        if token_json:
            try:
                token_data = json.loads(token_json)
                creds = Credentials.from_authorized_user_info(token_data, SCOPES)
            except json.JSONDecodeError:
                print("Warning: TOKEN_JSON is not valid JSON")

    # If there are no (valid) credentials available, let the user log in (ONLY LOCAL)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception as e:
                print(f"Error refreshing token: {e}")
                creds = None

        if not creds:
            # In production (serverless), we cannot run a local server. 
            # We must rely on the environment variable being correct.
            if os.getenv("VERCEL"):
                 raise RuntimeError("No valid credentials found in Vercel environment. Check TOKEN_JSON.")

            if not os.path.exists("credentials.json"):
                 # Try loading client config from env if file missing (handled below)
                 pass
            
            # Try loading from environment variable first
            google_creds_json = os.getenv("GOOGLE_CREDENTIALS_JSON")
            
            if google_creds_json:
                try:
                    client_config = json.loads(google_creds_json)
                    flow = InstalledAppFlow.from_client_config(
                        client_config, SCOPES
                    )
                except json.JSONDecodeError:
                     raise ValueError("GOOGLE_CREDENTIALS_JSON is not valid JSON")
            elif os.path.exists("credentials.json"):
                # Fallback to file
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", SCOPES
                )
            else:
                 raise FileNotFoundError("Neither GOOGLE_CREDENTIALS_JSON env var nor credentials.json file found.")
            
            print("Starting local server for auth...")
            creds = flow.run_local_server(port=8080)
            print("Auth successful")
        
        # Save the credentials for the next run (Local only)
        if not os.getenv("VERCEL"):
            with open("token.json", "w") as token:
                token.write(creds.to_json())

    return build("gmail", "v1", credentials=creds)

def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text, "html")
    message["to"] = to
    message["from"] = sender
    message["subject"] = subject
    return {"raw": base64.urlsafe_b64encode(message.as_bytes()).decode()}

def send_message(service, user_id, message):
    try:
        message = (
            service.users()
            .messages()
            .send(userId=user_id, body=message)
            .execute()
        )
        print(f'Message sent! Id: {message["id"]}')
        return message
    except HttpError as error:
        print(f"An error occurred sending message: {error}")
        return None
