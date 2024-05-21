import json
from passlib.context import CryptContext

from app.db.mysql import connect_to_db
from app.data.exceptions.DBException import DBException
class UserRepository:
    @staticmethod
    def find_user(username: str, password: str):
        """
        log in function
        """
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

        # connect to db
        conn = connect_to_db()

        if not conn:
            raise DBException

        cursor = conn.cursor()

        query = """
        select users.ID, username, password, users.role_id, GROUP_CONCAT(permissions.slug ORDER BY permissions.slug)
        from users
        left join permissions on permissions.role_id=users.role_id
        where users.username = %s
        """

        cursor.execute(query, [username])
        user_from_db = cursor.fetchone()
        cursor.close()
        conn.close()

        if not pwd_context.verify(password, user_from_db[2]):
            return None

        # return valid_user
        return {"ID": user_from_db[0], "username": user_from_db[1], "role_id": user_from_db[3], "access": user_from_db[4].split(',')}
    
    @staticmethod
    def find_user_from_token(_id: str, username:str):
        """
        Get user from DB using ID obtained from JWT token
        """

         # connect to db
        conn = connect_to_db()

        if not conn:
            raise DBException

        cursor = conn.cursor()

        query = """
        select users.ID, username, users.role_id, GROUP_CONCAT(permissions.slug ORDER BY permissions.slug)
        from users
        left join permissions on permissions.role_id=users.role_id
        where users.username = %s and users.ID= %s
        """

        cursor.execute(query, [username, _id])
        user_from_db = cursor.fetchone()
        cursor.close()
        conn.close()

        if not user_from_db:
            return None
        
        return {"ID": user_from_db[0], "username": user_from_db[1], "role_id": user_from_db[3], "access": user_from_db[3].split(',')}