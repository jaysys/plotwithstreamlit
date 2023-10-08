import os
import io
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Define the credentials file path (replace with your own JSON credentials file)
credentials_file = 'path/to/your/credentials.json'

# Define the API version and scope
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def authenticate_and_get_service():
    # Authenticate using the provided credentials
    creds = None
    try:
        creds = service_account.Credentials.from_service_account_file(
            credentials_file, scopes=SCOPES)
    except Exception as e:
        print(f"Authentication error: {e}")

    # Build the Google Drive API service
    service = build('drive', API_VERSION, credentials=creds)
    return service

def read_google_drive_file(service, file_name):
    try:
        # Search for the file by name
        results = service.files().list(q=f"name='{file_name}'").execute()
        files = results.get('files', [])

        if not files:
            print(f"No file found with the name '{file_name}'")
        else:
            # Get the first file (assuming there's only one with the same name)
            file_info = files[0]
            file_id = file_info['id']

            # Read the file content
            request = service.files().export_media(fileId=file_id, mimeType='text/plain')
            file_content = request.execute()

            return file_content

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Authenticate and get the Google Drive API service
    service = authenticate_and_get_service()

    # Specify the file name you want to read
    file_name = "hello.txt"

    # Read the content of the file
    file_content = read_google_drive_file(service, file_name)

    # Display the file content
    if file_content:
        print("File content:")
        print(file_content.decode('utf-8'))  # Assume the file is encoded in UTF-8

if __name__ == "__main__":
    main()
