from jose import jwt
from os import getenv
from datetime import timedelta, datetime, timezone

ACCESS_TOKEN_EXPIRE_MINUTES = 30

class JWTService:
    @staticmethod
    def create_access_token(user):
        try:
            expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            user = {**user, "exp": expire}
            return jwt.encode(user, getenv("SECRET_KEY"))
        except:
            return None
        
    
    @staticmethod
    def verify_token(token):
        try:
            return jwt.decode(token, getenv("SECRET_KEY"))
        except:
            return None