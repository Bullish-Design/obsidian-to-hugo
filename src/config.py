import os

from dotenv import load_dotenv

load_dotenv()

WEBSITE_BASE_URL = os.getenv("WEBSITE_BASE_URL")
