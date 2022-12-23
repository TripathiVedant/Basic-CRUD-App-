from pydantic import BaseModel
from typing import List, Literal, Optional

class User(BaseModel):
    username: str
    email:str
    password: str

class updateUser(BaseModel): 
    id:Optional[int]
    username: str
    password: str