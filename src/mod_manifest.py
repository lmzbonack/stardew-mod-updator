# Read in all manifest files found within a top level directory
import os
import json

from constants import MOD_DIRECTORY

class mod_manifest:

    def __init__(self):
        self.mod_directory = MOD_DIRECTORY
        self.installed_mods = {}

    def sanitize(self, dirtyString):
        '''Helper for discover_mods'''
        for char in dirtyString:
            if char[0] != '{':
                dirtyString = dirtyString[1:len(dirtyString)]
            else:
                break
        return dirtyString

    def discover_mods(self):
        '''Finds mods that are installed on the client'''
        for dirpath, dirnames, filenames in os.walk(self.mod_directory):
            for filename in [f for f in filenames if f == "manifest.json"]:
                fi = open(os.path.join(dirpath, filename), "r")
                fileString = fi.read()
                cleanFileString = self.sanitize(fileString)
                des = json.loads(cleanFileString)
                self.installed_mods[des["Name"]] = des
                fi.close()
        print(self.installed_mods)
        return self.installed_mods

MM = mod_manifest()
MM.discover_mods()
