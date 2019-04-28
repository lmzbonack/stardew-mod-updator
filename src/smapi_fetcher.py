import requests
import json

from win32api import GetFileVersionInfo, LOWORD, HIWORD

class smapi_fetcher:

    def __init__(self):
        self.url = 'https://api.github.com/repos/Pathoschild/SMAPI/releases/latest'
        self.session = requests.Session()
        self.session.headers.update(
            {
                'accept': "application/vnd.github.v3+json",
            }
        )
        
    def get_latest_release(self):
        '''API request to find latest version that needs to be donloaded'''
        response = self.session.request("GET", self.url)
        decoded = json.loads(response.text)
        return decoded['assets']

    def download_installer(self):
        '''Download installer for the latest mod'''
        assets = self.get_latest_release()
        # Find what file we actually want to download
        for asset in assets:
            for key, value in asset.items():
                if key == 'name':
                    if 'developer' not in value:
                        print(value)
                        print(asset['browser_download_url'])
                        return asset['browser_download_url']
    
    def get_current_version(self, filename):
        '''Returns the file version of the currently installed SMAPI version'''
        version = ".".join([str (i) for i in self.get_current_version_helper(filename)])
        print(version)
        return version

    def get_current_version_helper(self, filename):
        '''Helper for get_current_version'''
        try:
            info = GetFileVersionInfo(filename, "\\")
            ms = info['FileVersionMS']
            ls = info['FileVersionLS']
            return HIWORD (ms), LOWORD (ms), HIWORD (ls), LOWORD (ls)
        except:
            return "Unknown version"

    
SF = smapi_fetcher()

SF.download_installer()

SF.get_current_version('F:\Program Files (x86)\Steam\steamapps\common\Stardew Valley\StardewModdingAPI.exe')