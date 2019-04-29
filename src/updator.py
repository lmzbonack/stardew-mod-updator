from mod_manifest import mod_manifest
from api_wrapper import api_wrappper

class updator:

    def __init__(self):
        self.api = api_wrappper()
        self.local_mods = mod_manifest()
        # 2 api calls populate name, id, + other data for every tracked mod
        self.tracked_mods = {}
        self.untracked_mods = []
        self.outdated_mods = []
    
    def get_tracked_mods(self):
        '''Fetch all the mods that the user is tracking and load them into memory'''
        tracked_mods = self.api.get_tracked_mods()
        for mod in tracked_mods:
            if mod["domain_name"] == "stardewvalley":
                m_id = mod["mod_id"]
                mod_details = self.api.get_mod_file_details(m_id)
                mod_obj = {
                    "Id": mod_details["mod_id"],
                    "Name": mod_details["name"],
                    "Version": mod_details["version"],
                    "Game_Id": mod_details["game_id"]
                }
                mod_name = mod_details["name"]
                self.tracked_mods[mod_name] = mod_obj
        #print("Found " + str(len(self.tracked_mods)) + " tracked mod(s)")

    def get_installed_mods(self):
        '''Find all the mods that are installed locally'''
        self.local_mods.discover_mods()
        #print("Found " + str(len(self.local_mods.installed_mods)) + " installed mod(s)")


    def compare_versions(self):
        '''Compare tracked mods to the installed mods look for outdated mods and untracked mods'''
        for key in self.local_mods.installed_mods:
            if key not in self.tracked_mods:
                self.untracked_mods.append(self.local_mods.installed_mods[key]["Name"])
                print("Mod " + key + " was found in your installed mods but is a tracked mod in your Nexus account. Please track " + key)
            else:
                if self.local_mods.installed_mods[key]["Version"] != self.tracked_mods[key]["Version"]:
                    self.outdated_mods.append(self.tracked_mods[key])
        
        print("Found " + str(len(self.outdated_mods)) + " outdated mod(s)")
        print(self.outdated_mods)
        print("Found " + str(len(self.untracked_mods)) + " untracked mod(s)")
        print(self.untracked_mods)
        return self.outdated_mods


up = updator()
up.get_installed_mods()
up.get_tracked_mods()
up.compare_versions()
