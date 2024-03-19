import xml.etree.ElementTree as ET

# XML Class
# Loads the initial file and stores it in a variable
# Saves the edited file
class XML():
    def __init__(self, file):
        self.file = file
        self.ref = ET.parse(file) # auto loads the file
    
    # Saves the file
    def save(self, path):
        try: 
            self.ref.write(path)
        except Exception as e:
            return e
        

# Permissions Class
# Represents indivual permissions in the XML file
# Can be used to add, view, check and remove permissions in the file
class Permissions():
    def __init__(self, ref):
        self.ref = ref
    
    # Iterates through the file and returns a list of members with the given permission name.
    # If no permission ID does not match the name, it returns False
    def retrieveMembers(self, name):
        for permission in self.ref.ref.getroot().iter('Group'):
            if (permission.find('Id').text.lower() == name.lower()):
                return permission.find('Members')
        return False
    
    # Returns True if given steamid is in the given permission group
    def checkPermission(self, permission, steamid):
        members = self.retrieveMembers(permission)
        if (members == False):
            return False
        for member in members:
            if (member.text == steamid):
                return True
        return False
    
    # Retrieves all the permissions of a given steamid
    def retrievePermissions(self, steamid, include_hex = False):
        perm_list = []
        for permission in self.ref.ref.getroot().iter('Group'):
            if (self.checkPermission(permission.find('Id').text, steamid)):
                unit_perm = { "id" : permission.find('Id').text }
                if include_hex:
                    unit_perm = {
                        "name" : permission.find('Id').text,
                        "colour" : permission.find('Color').text
                    }
                perm_list.append(unit_perm)
        return perm_list
    
    # Returns a list of all permissions
    def listPermissions(self, include_hex=False):
        perm_list = []
        for permission in self.ref.ref.getroot().iter('Group'):
            unit_perm = { "id" : permission.find('Id').text }
            if include_hex:
                unit_perm = {
                    "name" : permission.find('Id').text,
                    "colour" : permission.find('Color').text
                }
            perm_list.append(unit_perm)
        return perm_list
    
    # Adds steamid to a given permission group
    # If the permission group does not exist or user already in group, return False
    # Else returns True
    def addPermission(self, permission, steamid):
        # Check if steamid is already in the group
        members = self.retrieveMembers(permission)
        if (members == False):
            return {"status" : False, "data" : f"No permission of name '{permission}' exists."}
        if (self.checkPermission(permission, steamid)):
            return {"status" : False, "data" : f"User {steamid} already has permission."}
        ET.SubElement(members, 'Member').text = steamid
        self.ref.save(self.ref.file)
        return {"status" : "True", "data": ""}
    
    # Removes steamid from a give permission group
    # If the user if not in the permssion group, returns False
    # If the group does not exist, returns False
    # Else returns True
    def removePermission(self, permission, steamid):
        members = self.retrieveMembers(permission)
        if (members == False):
            return False
        if (self.checkPermission(permission, steamid) == False):
            return False
        for member in members:
            if (member.text.lower() == steamid.lower()):
                members.remove(member)
                self.ref.save(self.ref.file)
                return True
