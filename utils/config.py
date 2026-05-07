import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL")
    TENANT_NAME = os.getenv("TENANT_NAME")
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")