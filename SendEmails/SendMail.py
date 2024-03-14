import base64
import os
import pandas as pd
from email.message import EmailMessage
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import mimetypes
import threading
import time
import concurrent.futures
import logging

SCOPES = ['https://www.googleapis.com/auth/gmail.send', 'https://www.googleapis.com/auth/gmail.compose']

def get_credentials():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds


def msg_text():
  content = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Volunteer Appreciation Email</title>
    </head>
    <body>
        <div style="font-family: Arial, sans-serif; background-color: #f2f2f2; padding: 20px;">
            <h2 style="color: #333333;">Volunteer Appreciation Email</h2>
            <p style="color: #333333;">Dear Volunteers,</p>
            <p style="color: #333333;">I wanted to take a moment to express my heartfelt appreciation for your valuable contribution in testing the Python script for automated certificate generation and sending emails. Your dedication and efforts have been instrumental in ensuring the success of this project.</p>
            <p style="color: #333333;">Your attention to detail, thoroughness, and commitment to quality have greatly contributed to the overall success of our endeavor. The feedback and insights you provided during the testing phase have been invaluable in refining the script and making it more robust.</p>
            <p style="color: #333333;">I am truly grateful for your time, expertise, and enthusiasm. Your hard work and commitment have made a significant impact, and I cannot thank you enough for your dedication to this project.</p>
            <p style="color: #333333;">Once again, thank you for your exceptional efforts. Your contributions have not gone unnoticed, and I am truly grateful for your support.</p>
            <p style="color: #333333;">Regards,</p>
            <p style="color: #333333;">Atharv Sathe</p>
        </div>
    </body>
    </html>
  '''
  return content

# Set up logging
logging.basicConfig(filename='./Logs/test.txt', level=logging.INFO)


# Create a semaphore that allows two emails to be sent per second
semaphore = threading.Semaphore(2)

def gmail_send_attachment(name, regNo, email):
    # Acquire the semaphore
    creds = get_credentials()
    with semaphore:
        try:
            message_text = msg_text()

            mime_message = EmailMessage()

            # headers
            mime_message["To"] = f"{email}"
            mime_message["From"] = "atharvsathe28704@gmail.com"
            mime_message["Subject"] = "This is a Test Mail!"
            mime_message.set_content(message_text, subtype='html')


            # attachment
            attachment_filename = f"./Attachments/{regNo}.png"
            # guessing the MIME type
            type_subtype, _ = mimetypes.guess_type(attachment_filename)
            maintype, subtype = type_subtype.split("/")
            with open(attachment_filename, "rb") as fp:
              attachment_data = fp.read()
            # Define the service variable
            service = build('gmail', 'v1', credentials=creds)

            filename = os.path.basename(attachment_filename)
            mime_message.add_attachment(attachment_data, maintype, subtype, filename=filename)

            encoded_message = base64.urlsafe_b64encode(mime_message.as_bytes()).decode()

            create_message = {"raw": encoded_message}
            send_message = (
                service.users()
                .messages()
                .send(userId="me", body=create_message)
                .execute()
            )
            print(f'Mail Sent to {name} >> Message id: {send_message["id"]}')
            logging.info(f'Sent email to {email}, message id: {send_message["id"]}')
        except HttpError as error:
            print(f"An error occurred: {error}")
            logging.error(f'Failed to send email to {email}: {error}')
            send_message = None
        # Release the semaphore after a delay
        time.sleep(0.5)
    return send_message

def get_details():
    csv = pd.read_csv('../CSVs/test.csv')
    nameList = csv['Name'].tolist()
    regList = csv['Registration Number'].tolist()
    emailList = csv['Email'].tolist()

    # Use a thread pool to send emails concurrently
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(gmail_send_attachment, nameList, regList, emailList)


if __name__ == "__main__":
  get_details()
