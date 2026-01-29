import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# --------------------------------
# GOOGLE CALENDAR CONFIG
# --------------------------------
SCOPES = ['https://www.googleapis.com/auth/calendar']

# --------------------------------
# AUTHENTICATION
# --------------------------------
def authenticate_calendar():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return build("calendar", "v3", credentials=creds)

# --------------------------------
# SCHEDULE MEETING ACTION
# --------------------------------
def schedule_meeting(task):
    print(f"\n📅 Scheduling meeting: {task['title']}")

    service = authenticate_calendar()

    # Ensure RFC3339 datetime format
    start_time = task["start"] + "+05:30"
    end_time = task["end"] + "+05:30"

    event = {
        "summary": task["title"],
        "start": {
            "dateTime": start_time,
            "timeZone": "Asia/Kolkata"
        },
        "end": {
            "dateTime": end_time,
            "timeZone": "Asia/Kolkata"
        },
        "attendees": [{"email": email} for email in task["attendees"]]
    }

    created_event = service.events().insert(
        calendarId="primary",
        body=event,
        sendUpdates="all"
    ).execute()

    print("✅ Meeting scheduled")
    print("🔗 Event link:", created_event.get("htmlLink"))