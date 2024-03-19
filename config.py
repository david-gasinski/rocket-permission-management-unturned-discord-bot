from os import getenv
from dotenv import load_dotenv

# load environmental variables
load_dotenv() 

settings = {
    "perm_config": getenv("PERMISSIONS_CONFIG"),
    "kits_config": getenv("KITS_CONFIG"),
    "discord_token" : getenv("DISCORD_TOKEN"), 
    "prefix" : "!"
}