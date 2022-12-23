
from payloads.requestpayloads import User, updateUser
from dao.user_dao import UserDAO

from fastapi import status
from fastapi.exceptions import HTTPException

class UserService():
    def read_data(self):
        user_data = UserDAO.read_data()
        if not user_data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="No Record found!")
        return user_data

    def read_user_data(self,id: int):
        user_data = UserDAO.read_user_data(id)
        if not user_data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Record do not exists")
        return user_data

    def write_data(self, user: User):
        existing_data=UserDAO.findByEmail(user.email)
        if existing_data:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Email already Exists!")

        user_data=UserDAO.create_user(user=user)
        return user_data

    def update_data(self, id:int, user: updateUser):
        user_data = UserDAO.read_user_data(id)
        if not user_data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User do not exists")
        return UserDAO.update_data(id, user)
    
    def delete_data(self, id: int):
        user_data = UserDAO.read_user_data(id)
        if not user_data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User do not exists")
        UserDAO.delete_data(id)
        return user_data

UserService = UserService()