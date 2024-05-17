import json
from passlib.context import CryptContext

class UserRepository:
    @staticmethod
    def find_user(username: str, password: str):
        """
        log in function
        """
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        f = open('./app/data/users/docs.json')
        data = json.load(f)

        valid_user = None

        for i in range(0, len(data)):
            user = data[i]

            if user and user["username"] == username and pwd_context.verify(password, user["password"]):
                valid_user = user
                break;

        return valid_user
    
    @staticmethod
    def find_user_from_token(_id: str, username:str):
        """
        Get user from DB using ID obtained from JWT token
        """
        f = open('./app/data/users/docs.json')
        data = json.load(f)

        valid_user = None

        for i in range(0, len(data)):
            user = data[i]

            if user and user["username"] == username and user["_id"] == _id:
                valid_user = user
                break;

        return valid_user