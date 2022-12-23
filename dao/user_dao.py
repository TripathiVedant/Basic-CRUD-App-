from payloads.requestpayloads import User, updateUser
from models.users import user_model
from config.db import conn

class UserDAO():

    def findByEmail(self,email: str):
        return conn.execute(user_model.select().where(user_model.c.email==email)).fetchall()

    def create_user(self,user: User):
        conn.execute(user_model.insert().values(
        username=user.username,
        email=user.email,
        password=user.password
        ))
        return self.findByEmail(user.email)

    def read_data(self):
        return conn.execute(user_model.select()).fetchall()
    
    def read_user_data(self,id: int):
        return conn.execute(user_model.select().where(user_model.c.id==id)).fetchall()

    def update_data(self, id:int, user: updateUser):
        conn.execute(user_model.update().values(
            username=user.username,
            password=user.password
        ).where(user_model.c.id==id))
        return self.read_user_data(id)

    def delete_data(self, id: int):
        conn.execute(user_model.delete().where(user_model.c.id==id))
        

UserDAO=UserDAO()