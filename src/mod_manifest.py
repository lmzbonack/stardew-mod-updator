# Read in all manifest files found within a top level directory
import os
import json

from win32api import GetFileVersionInfo, LOWORD, HIWORD

mod_directory = "F:\Program Files (x86)\Steam\steamapps\common\Stardew Valley\Mods"

class mod_manifest:

    def __init__(self):
        self.mod_directory = mod_directory
        self.installed_mods = {}

    def sanitize(self, dirtyString):
        for char in dirtyString:
            if char[0] != '{':
                dirtyString = dirtyString[1:len(dirtyString)]
            else:
                break
        return dirtyString

    def discover_mods(self):
        for dirpath, dirnames, filenames in os.walk(mod_directory):
            for filename in [f for f in filenames if f == "manifest.json"]:
                fi = open(os.path.join(dirpath, filename), "r")
                fileString = fi.read()
                cleanFileString = self.sanitize(fileString)
                des = json.loads(cleanFileString)
                self.installed_mods[des["Name"]] = des
                fi.close()
        return self.installed_mods

    def get_current_version(self, filename):
        version = ".".join([str (i) for i in self.get_current_version_helper(filename)])
        print(version)
        return version

    def get_current_version_helper(self, filename):
        try:
            info = GetFileVersionInfo(filename, "\\")
            ms = info['FileVersionMS']
            ls = info['FileVersionLS']
            return HIWORD (ms), LOWORD (ms), HIWORD (ls), LOWORD (ls)
        except:
            return "Unknown version"

MM = mod_manifest()

MM.get_current_version('F:\Program Files (x86)\Steam\steamapps\common\Stardew Valley\StardewModdingAPI.exe')
