import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    NEWS_API_KEY = os.getenv('NEWS_API_KEY', 'default_if_missing')
