import requests
import json

url = 'https://github.com/Pathoschild/SMAPI/releases/download/2.11.1/SMAPI-2.11.1-installer.zip'

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
        response = self.session.request("GET", self.url)
        decoded = json.loads(response.text)
        return decoded['assets']

    def download_installer(self):
        assets = self.get_latest_release()
        # Find what file we actually want to download
        for asset in assets:
            for key, value in asset.items():
                if key == 'name':
                    if 'developer' not in value:
                        print(value)
                        print(asset['browser_download_url'])
                        return asset['browser_download_url']

    
SF = smapi_fetcher()

SF.download_installer()