
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

def upload_video(file_path):
    scopes = ["https://www.googleapis.com/auth/youtube.upload"]
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        "credentials.json", scopes)
    credentials = flow.run_local_server()
    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)

    request = youtube.videos().insert(
        part="snippet,status",
        body={
          "snippet": {
            "title": "Daily Clip",
            "description": "Auto-generated Shorts",
            "tags": ["shorts", "ai", "clips"],
            "categoryId": "24"
          },
          "status": {
            "privacyStatus": "public"
          }
        },
        media_body=file_path
    )
    response = request.execute()
    print(response)
