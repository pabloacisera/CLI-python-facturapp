import os

from dotenv import load_dotenv

load_dotenv('.env.development')

API_URL=os.getenv("API_URL")
SECRET_KEY=os.getenv("SECRET_KEY")

if not API_URL:
    raise ValueError("API_URL not defined")

if not SECRET_KEY:
    raise ValueError("SECRET_KEY not defined")