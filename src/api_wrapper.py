import requests

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
        url = self.base_url + "games/stardewvalley/mods/{}.json".format(mod_id)
        response = self.session.request("GET", url)
        print(response.text)
        return response.text

    def get_tracked_mods(self):
        url = self.base_url + "user/tracked_mods.json"
        response = self.session.request("GET", url)
        print(response.text)
        return response.text
