import json
from passlib.context import CryptContext

class UserRepository:
    @staticmethod
    def find_user(username: str, password: str):
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