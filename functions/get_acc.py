from dotenv import load_dotenv
import requests
import json
import os
import functions.champion as champion
import functions.match_game as m

master_champ_list = champion.create_champ_list()

class Champ_Mastery:
    def __init__(self, response: dict):
        self.json_info = response
        self.champ_info = master_champ_list[str(response["championId"])]
    
    def print_info(self):
        master = self.json_info["championLevel"]
        print(f"{self.champ_info.name}: {self.champ_info.title} - {master}")
        # for key in self.json_info:
        #     print(f"{key}: {self.json_info[key]}")

class Riot_Acc:
    def __init__(self, api_key, user, tag):
        self.api_key = api_key
        acc_url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{user}/{tag}"
        headers = {
            "X-Riot-Token": self.api_key
        }
        response = requests.get(acc_url, headers=headers)
        if(response.status_code != 200):
            raise Exception(f"API Error in Riot_Acc Constructor: {response.status_code}")
        mp = json.loads(response.text) 
        self.api_key = api_key
        self.puuid = mp["puuid"]
        self.gameName = mp["gameName"]
        self.tagLine = mp["tagLine"]
        self.champList = []
    
    def print_info(self):
        print(f"puuid: {self.puuid}\nusername: {self.gameName}#{self.tagLine}")
    
    def get_puuid(self):
        return self.puuid
    
    def get_champ_mastery(self):
        # https://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json
        url = f"https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{self.puuid}"
        headers = {
            "X-Riot-Token": self.api_key
        }
        response = requests.get(url, headers=headers)
        if(response.status_code != 200):
            raise Exception(f"API Error in get_champ_mastery(): {response.status_code}")
        mp = json.loads(response.text)
        
        for key in mp:
            self.champList.append(Champ_Mastery(key))
    
        for champ in self.champList:
            champ.print_info()
    
    def get_matches_ids(self) -> list:
        url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{self.puuid}/ids"
        headers = {
            "X-Riot-Token": self.api_key
        }
        response = requests.get(url, headers=headers)
        if(response.status_code != 200):
            raise Exception(f"API Error in get_matches(): {response.status_code}")
            
        return json.loads(response.text)
    
    def parse_matches_ids(self):
        self.match_history = {}
        match_ids = self.get_matches_ids()
        for match_id in match_ids:
            game = m.Match_Game(self.api_key, match_id)
            self.match_history[match_id] = game.get_player_stats(self.puuid)
        return self.match_history
