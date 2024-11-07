from pydantic_settings import BaseSettings
import os
import dotenv

dotenv.load_dotenv()

class Settings(BaseSettings):
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY")
    # Google Cloud Settings
    GOOGLE_CLOUD_PROJECT: str = os.getenv("GOOGLE_CLOUD_PROJECT")
    GOOGLE_CLOUD_REGION: str = os.getenv("GOOGLE_CLOUD_REGION") 
    GOOGLE_APPLICATION_CREDENTIALS: str = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

settings = Settings()

