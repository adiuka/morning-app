import os.path
from datetime import datetime, timedelta, timezone
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]


def get_day_range(date: datetime):
    start_of_day = datetime(date.year, date.month, date.day, tzinfo=timezone.utc)
    end_of_day = start_of_day + timedelta(days=1)
    return start_of_day.isoformat(), end_of_day.isoformat()


def fetch_calendar_data():
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

    try:
        service = build("calendar", "v3", credentials=creds)

        target_date = datetime.now(tz=timezone.utc)
        time_min, time_max = get_day_range(target_date)
        print("Getting the upcoming 10 Events")
        events_result = (
            service.events()
            .list(
                calendarId="primary",
                timeMin=time_min,
                timeMax=time_max,
                maxResults=10,
                singleEvents=True,
                orderBy="startTime"
            )
            .execute()
        )
        events = events_result.get("items", [])

        if not events:
            return ["📅 No events today!"]
        
        output = []
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            end = event["end"].get("dateTime", event["end"].get("date"))
            start_time = datetime.fromisoformat(start).strftime("%H:%M")
            end_time = datetime.fromisoformat(end).strftime("%H:%M")
            summary = event.get("summary", "No Title")
            output.append(f"📅 {start_time} - {end_time} | {summary}")
        return output

    except HttpError as error:
        print(f"An Error occured: {error}")
