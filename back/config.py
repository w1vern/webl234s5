from enum import Enum
import json
import os
from dotenv import load_dotenv

load_dotenv()

SECRET = os.getenv('SECRET')

class Config:
    auth_session_lifetime = 60*30