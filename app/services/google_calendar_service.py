import httpx
from app.core.config import settings


class GoogleCalendarService:
    @staticmethod
    async def create_event(summary: str, start_time: str, end_time: str, attendees: list[str]):
        headers = {
            "Authorization": f"Bearer {settings.GOOGLE_ACCESS_TOKEN}",
            "Content-Type": "application/json"
        }
        payload = {
            "summary": summary,
            "start": {"dateTime": start_time},
            "end": {"dateTime": end_time},
            "attendees": [{"email": email} for email in attendees],
            "conferenceData": {
                "createRequest": {
                    "requestId": "recruitment-interview"
                }
            }
        }

        async with httpx.AsyncClient() as client:
            resp = await client.post(
                f"{settings.GOOGLE_CALENDAR_API_URL}/calendars/primary/events?conferenceDataVersion=1",
                headers=headers,
                json=payload
            )
            if resp.is_success:
                data = resp.json()
                return {
                    "google_event_id": data.get("id"),
                    "meeting_link": data.get("hangoutLink")
                }
            return {"google_event_id": None, "meeting_link": None}