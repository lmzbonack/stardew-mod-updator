import requests
import json

from env_vars import get_api_key

class api_wrappper:

    def __init__(self):
        self.base_url = "https://api.nexusmods.com/v1/"
        self.session = requests.Session()
        self.session.headers.update(
            {
                "user-agent": "Python Script",
                "apikey": get_api_key(),
                "content-type": "application/json"
            }
        )

    def get_mod_file_details(self, mod_id):
        # Returns the details for a specific mod based on an id
        url = self.base_url + "games/stardewvalley/mods/{}.json".format(mod_id)
        response = self.session.request("GET", url)
        return json.loads(response.text)

    def get_tracked_mods(self):
        # Returns the mods that an account has tracked.
        url = self.base_url + "user/tracked_mods.json"
        response = self.session.request("GET", url)
        return json.loads(response.text)