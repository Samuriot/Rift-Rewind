from dotenv import load_dotenv
import requests
import json
import os

load_dotenv()
api_key = os.getenv("RIOT_API")

class Riot_Acc:
    def __init__(self, api_key, user, tag):
        acc_url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{user}/{tag}"
        headers = {
            "X-Riot-Token": api_key
        }
        response = requests.get(acc_url, headers=headers)
        mp = json.loads(response.text) 
        self.puuid = mp["puuid"]
        self.gameName = mp["gameName"]
        self.tagLine = mp["tagLine"]
    
    def get_info(self):
        print(f"puuid: {self.puuid}\nusername: {self.gameName}#{self.tagLine}")

test.get_info()

    