from os import getenv
from dotenv import load_dotenv

# load environmental variables
load_dotenv() 

settings = {
    "perm_config_file": getenv["PERMISSIONS_CONFIG"],
    "kits_config_file": getenv["KITS_CONFIG"],
    "discord_token" : getenv["DISCORD_TOKEN"], 
    "prefix" : "!"
}