from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Permission(BaseModel):
    name: str
    members: list[str]

class User(BaseModel):
    steamid: str
    roles: list[str]

# base commands
# add / remove user to perm
# view / search all members of a perm
# filter by steamid and permission
# view all members of a steam id
# view list of all permisisons

# interactable
# add new permission
    