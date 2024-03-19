# base commands
# add / remove user to perm - can be done by discord id if user has steam linked
# view / search all members of a perm
# filter by steamid and permission
# view all perms of a steam id
# view list of all permisisons

# interactable
# add new permission

from typing import Optional
from fastapi import FastAPI
from fastapi import APIRouter
from datetime import datetime
from pydantic import BaseModel

from perms.xml_edit import XML
from perms.xml_edit import Permissions
from config import settings
from util.logger import Logger

# types of POST req bodies

class GetPermission(BaseModel):
    include_hex: bool = False
    request_origin: str

class AddPermission(BaseModel):
    steam_id: str
    permissions: list[str]

class Routes():
    def __init__(self, permissions, kits, logger):
        self.router = APIRouter()
        self.permissions = Permissions(XML(permissions))
        self.kits = kits
        self.logger = logger
        self.logger_instance = logger.get_logger()
        self._init_routes()

    def _init_routes(self):
        self.router.add_api_route('/permissions/list', self.post_list_permissions,methods=['GET', 'POST'])
        self.router.add_api_route('/permissions/add', self.post_add_user_permission, methods=['POST'])
    
    async def post_list_permissions(self, args: GetPermission):
        try:
            data = self.permissions.listPermissions(args.include_hex) 
            self.logger.log_request(args.request_origin, self.post_list_permissions.__name__, True)
            return {"status" : True, "data" : data}
        except Exception as e:
            self.logger.log_request(args.request_origin, self.post_list_permissions.__name__, False)
            self.logger_instance.error("Exception Stacktrace", exc_info=True)
            return {"status" : False , "data" : []}
        
    async def post_add_user_permission(self, args: AddPermission):
        try:
            for permission in args.permissions:
                res = self.permissions.addPermission(permission, args.steam_id) # in the future, validate steam_id
        except Exception as e:
            return

app = FastAPI()
logger = Logger(f'util/logs/api/{datetime.today( ).strftime("%Y-%m-%d")}.log')
api_router = Routes(settings['perm_config'], settings['kits_config'], logger)
app.include_router(api_router.router)
