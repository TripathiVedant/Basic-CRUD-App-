from fastapi import APIRouter
from services.user_service import UserService
from payloads.requestpayloads import User, updateUser
router = APIRouter(prefix="/user", tags=["user"])

@router.get("/")
async def read_data():
    """api to read all the users

    Returns:
        list of users
    """
    return UserService.read_data()

@router.get("/{id}")
async def read_user_data(id: int):
    """api to read user with given id

    Arguments:
        id: int

    Returns:
        user's detail
    """
    return UserService.read_user_data(id)


@router.post("/", status_code=201)
async def write_data(user: User):
    """api to create a new user

    Arguments:
        User: User details

    Returns:
        Updated list of all Users.
    """
    return UserService.write_data(user)

@router.put("/{id}")
async def update_data(id:int, user: updateUser):
    """api to update user with given id

    Arguments:
        id: int
        user: updateUser, updated username and password

    Returns:
        Updated list of all Users.
    """
    
    return UserService.update_data(id,user)

@router.delete("/{id}")
async def delete_data(id: int):
    """api to update user with given id

    Arguments:
        id: int
        user: updateUser, updated username and password

    Returns:
        Updated list of all Users.
    """
    return UserService.delete_data(id)