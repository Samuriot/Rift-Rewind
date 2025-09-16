from dotenv import load_dotenv
import requests
import json
import os

load_dotenv()
api_key = os.getenv("RIOT_API")

class Champ_Mastery:
    def __init__(self, response: dict):
        self.json_info = response
    
    def print(self):
        for key in self.json_info:
            print(f"{key}: {self.json_info[key]}")

class Riot_Acc:
    def __init__(self, api_key, user, tag):
        acc_url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{user}/{tag}"
        headers = {
            "X-Riot-Token": api_key
        }
        response = requests.get(acc_url, headers=headers)
        mp = json.loads(response.text) 
        self.api_key = api_key
        self.puuid = mp["puuid"]
        self.gameName = mp["gameName"]
        self.tagLine = mp["tagLine"]
        self.champList = []
    
    def get_info(self):
        print(f"puuid: {self.puuid}\nusername: {self.gameName}#{self.tagLine}")
    
    def get_champ_mastery(self):
        # https://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json
        url = f"https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{self.puuid}"
        headers = {
            "X-Riot-Token": api_key
        }
        response = requests.get(url, headers=headers)
        mp = json.loads(response.text)
        
        for key in mp:
            self.champList.append(Champ_Mastery(key))
        
        for champ in self.champList:
            print(champ.print())
