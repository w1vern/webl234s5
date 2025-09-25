
import os

from dotenv import load_dotenv

load_dotenv()

SECRET = os.getenv('SECRET')

class Config:
    auth_session_lifetime = 60*60*24
    basket_lifetime = 3600*24
    worker_count = 100