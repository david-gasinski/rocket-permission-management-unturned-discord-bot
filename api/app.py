# base commands
# add / remove user to perm - can be done by discord id if user has steam linked
# view / search all members of a perm
# filter by steamid and permission
# view all members of a steam id
# view list of all permisisons

# interactable
# add new permission

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from cbfa import ClassBased


app = FastAPI() # new fast api instance
wrapper = ClassBased(app) 

# types

class SteamID(BaseModel):
    steam_64: str


