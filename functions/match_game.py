# match_game.py
# defines the Player_Performance and Match_Game classes which represent the data from
# a LoL game, as well as an individual player's performance based on a search

import requests
import json

# match_url global variable
match_url  = "https://americas.api.riotgames.com/lol/match/v5/matches/"

# Player_Performance class which represents an individual's performance across a game of LoL
# used by Riot_Acc and Match_Game classes via composition
class Player_Performance:
    # __init__ constructor
    def __init__(self, id, user, dump, role):
        self.id = id
        self.user = user
        self.json_file = dump
        self.role = role
        
    # load_stats method will parse self.json_file for information from Riot API
    # TODO: WIP currently, need to add more areas to parse
    def load_stats(self):
        self.kills = self.json_file["kills"]
        self.deaths = self.json_file["deaths"]
        self.assists = self.json_file["assists"]
        if self.deaths != 0:
            self.kda = round((self.kills + self.assists) / self.deaths, 3)
        else:
            self.kda = self.kills + self.assists
        self.gold = self.json_file["goldEarned"]
    
    # __str__ getter method
    def __str__(self):
        return json.dumps(self.json_file, indent=4)
    
    # getter methods for member data
    def get_KDA(self):
        return f"{self.kills}/{self.deaths}/{self.assists} - {self.kda}"
    
    def get_kills(self):
        return self.kills
    
    def get_deaths(self):
        return self.deaths
    
    def get_assists(self):
        return self.assists

# Match_Game Class, which represents an single LoL game, which should host the performance of each player
# based on an API call to the RIOT API, class will throw an exception will API call fails
class Match_Game:
    # load_players method which will go through each participant in the game & create a Player_Performance Object
    # optional method to be called, to prevent constantly call this method
    def load_players(self):
        gameData = self.json_resp["info"]["participants"]
        for entry in gameData:
            user = Player_Performance(entry["puuid"], entry["riotIdGameName"] + "#" + entry["riotIdTagline"], entry, entry["individualPosition"])
            user.load_stats()
            self.players.append(user)
    
    # __init__ constructor, which will throw an exception if Riot API fails        
    def __init__(self, api_key, match_id):
        self.players = []
        self.api_key = api_key
        self.match_id = match_id
        self.api_req = match_url + match_id
        
        headers = {
            "X-Riot-Token": self.api_key
        }
        
        self.json_resp = requests.get(self.api_req, headers=headers)        
        if(self.json_resp.status_code != 200):
            raise Exception(f"API Error in get_matches(): {self.json_resp.status_code}")
        
        self.json_resp = json.loads(self.json_resp.text)
        self.load_players()
        
    # getter and printer methods for Match_Game class
    def get_player_stats(self, user: str) -> Player_Performance | None:
        for player in self.players:
            if user == player.id:
                return player
        return None
            
    def print_basic_stats(self):
        for user in self.players:
            print(f"{str(user)}: {user.get_KDA()} - {user.gold} total gold")

    def print_details(self):
        print(json.dumps(self.json_resp, indent=4))