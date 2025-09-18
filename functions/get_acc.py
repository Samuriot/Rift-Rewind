# get_acc.py
# defines the Champ_Mastery & Riot_Acc Class Definitions, which are integral for getting a player's stats

from dotenv import load_dotenv
import requests
import json
import os
import functions.champion as champion
import functions.match_game as m

# dictionary with all champions as a global var
master_champ_list = champion.create_champ_list()

# Champ_Mastery Class which defines a player's specific experience with a champion
# hosts all the data from an API call to the RiotAPI
# future plan, link to Champion object
class Champ_Mastery:
    # __init__ constructor
    def __init__(self, response: dict):
        self.json_info = response
        self.champ_info = master_champ_list[str(response["championId"])]
    
    # print_info method to print the contents of Champ_Mastery
    def print_info(self):
        master = self.json_info["championLevel"]
        print(f"{self.champ_info.name}: {self.champ_info.title} - {master}")
        # for key in self.json_info:
        #     print(f"{key}: {self.json_info[key]}")

# Riot_Acc Class which defines an instance of a player's account, based on Riot API
# Performs several API calls to the RIOT API to get information such as Champion Mastery
# Also obtains and stores a user's previous match history via json
class Riot_Acc:
    # __init__ constructor that forms a Riot_Acc object based on Riot API Call
    # will throw an error based on results of Riot API
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
    
    # print_info will print out a user's puuid & Riot Tag
    def print_info(self) -> None:
        print(f"puuid: {self.puuid}\nusername: {self.gameName}#{self.tagLine}")
    
    # get_puuid getter method
    def get_puuid(self) -> str:
        return self.puuid
    
    # get_champ_mastery will perform an API call to get a user's complete champion mastery history
    # method will throw an exception if API call fails
    def get_champ_mastery(self) -> None:
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
    
    # get_matches_ids method will perform an API call and create a list of the most recent 10 matches
    def get_matches_ids(self) -> list:
        url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{self.puuid}/ids"
        headers = {
            "X-Riot-Token": self.api_key
        }
        response = requests.get(url, headers=headers)
        if(response.status_code != 200):
            raise Exception(f"API Error in get_matches(): {response.status_code}")
            
        return json.loads(response.text)
    
    # parse_matches_ids will parse information from get_matches_ids and create dictionaries with the information
    def parse_matches_ids(self) -> dict:
        self.match_history = {}
        match_ids = self.get_matches_ids()
        for match_id in match_ids:
            game = m.Match_Game(self.api_key, match_id)
            self.match_history[match_id] = game.get_player_stats(self.puuid)
        return self.match_history
    
    def compile_match_stats(self):
        # create a singular json, which parses every single match in self.match_history
        # and compiles all the combined stats present
        compiled_stats = {}
        for key, val in self.match_history.items():
            for category, content in val.json_file.items():
                if type(content) == int:
                    if category not in compiled_stats:
                        compiled_stats[category] = 0
                    compiled_stats[category] += content
                elif type(content) == str:
                    if category not in compiled_stats:
                        compiled_stats[category] = []
                    compiled_stats[category].append(content)
                elif type(content) == dict:
                    pass
                elif type(content) == bool:
                    if category not in compiled_stats:
                        compiled_stats[category] = 0
                    if content is True:
                        compiled_stats[category] += 1
        
        compiled_stats.pop("puuid")
        compiled_stats.pop("riotIdGameName")
        compiled_stats.pop("riotIdTagline")
        compiled_stats.pop("summonerId")
        compiled_stats.pop("summonerName")
        compiled_stats.pop("summonerLevel")
        
        for key, val in compiled_stats.items():
            print(f"{key}: {val}")
            
    
    # get_recent_KDA will summarize all kills, deaths, and assists from self.match_history
    # and return a cummulative KDA based on performane
    def get_recent_KDA(self) -> float:
        num_kills = 0
        num_deaths = 0
        num_assists = 0
        for key, val in self.match_history.items():
            num_kills += val.get_kills()
            num_deaths += val.get_deaths()
            num_assists += val.get_assists()
        
        kda = (num_kills + num_assists) / num_deaths 
        
        print(f"{num_kills}/{num_deaths}/{num_assists} - {kda}")
        return kda
