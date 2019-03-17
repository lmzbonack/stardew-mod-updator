# Read in all manifest files found within a top level directory
import os
import json

mod_directory = "F:\Program Files (x86)\Steam\steamapps\common\Stardew Valley\Mods"

class mod_manifest:

    def __init__(self,):
        self.mod_directory = mod_directory
        self.mod_list = []

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
                self.mod_list.append(des)
                fi.close()

        print(self.mod_list)
        print(self.mod_list[0]['Version'])

tester = mod_manifest()
tester.discover_mods()
