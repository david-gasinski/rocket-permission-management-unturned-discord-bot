# EVERY HOUR THE PERMISSIONS FILE WILL BE BACKED UP
import datetime
import time

# clones files contents into a new file
def backup(name, origin, destination):
    # validate if destination is valid
    if destination[-1] == '/':
        destination += '/'

    with open(origin, "r") as current:
        data = current.read()
        with open (destination + name, "w") as backup:
            backup.write(data)
            backup.close()
        current.close()
