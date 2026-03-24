import httpx
from app.core.config import settings


class LinkedInService:
    @staticmethod
    async def import_profile(profile_id: str):
        headers = {"Authorization": f"Bearer {settings.LINKEDIN_ACCESS_TOKEN}"}
        async with httpx.AsyncClient() as client:
            resp = await client.get(
                f"{settings.LINKEDIN_API_URL}/v2/people/(id:{profile_id})",
                headers=headers
            )
            return {"status_code": resp.status_code, "data": resp.text}

    @staticmethod
    async def publish_job(payload: dict):
        headers = {
            "Authorization": f"Bearer {settings.LINKEDIN_ACCESS_TOKEN}",
            "Content-Type": "application/json"
        }
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                f"{settings.LINKEDIN_API_URL}/jobs",
                headers=headers,
                json=payload
            )
            return {"status_code": resp.status_code, "data": resp.text}