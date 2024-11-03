
from pydantic import BaseModel

class LoginData(BaseModel):
    phone: str
    password: str

class RegisterData(BaseModel):
    phone: str
    password: str
    password_repeat: str

class GetAuthData(BaseModel):
    is_auth: bool
    phone: str
