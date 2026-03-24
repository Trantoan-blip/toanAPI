from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Recruitment HR API"
    SECRET_KEY: str = "super-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    DATABASE_URL: str = "sqlite:///./recruitment.db"

    LINKEDIN_API_URL: str = "https://api.linkedin.com"
    LINKEDIN_ACCESS_TOKEN: str = ""

    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USERNAME: str = ""
    SMTP_PASSWORD: str = ""
    EMAIL_FROM: str = "hr@example.com"

    GOOGLE_CALENDAR_API_URL: str = "https://www.googleapis.com/calendar/v3"
    GOOGLE_ACCESS_TOKEN: str = ""

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()