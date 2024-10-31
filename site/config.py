import os
from dotenv import load_dotenv


load_dotenv()

SECRET = os.getenv('SECRET')

class Config:
    access_token_lifetime = 600
    refresh_token_lifetime = 2592000
    algorithm = 'HS256'