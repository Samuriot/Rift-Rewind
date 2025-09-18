import requests
import json

match_url  = "https://americas.api.riotgames.com/lol/match/v5/matches/"

class Player_Performance:
    def __init__(self, id, user, dump, role):
        self.id = id
        self.user = user
        self.json_file = dump
        self.role = role
        
    def load_stats(self):
        self.kills = self.json_file["kills"]
        self.deaths = self.json_file["deaths"]
        self.assists = self.json_file["assists"]
        if self.deaths != 0:
            self.kda = round((self.kills + self.assists) / self.deaths, 3)
        else:
            self.kda = self.kills + self.assists
        self.gold = self.json_file["goldEarned"]
    
    def __str__(self):
        return json.dumps(self.json_file, indent=4)
    
    def get_KDA(self):
        return f"{self.kills}/{self.deaths}/{self.assists} - {self.kda}"

class Match_Game:
    def load_players(self):
        gameData = self.json_resp["info"]["participants"]
        for entry in gameData:
            user = Player_Performance(entry["puuid"], entry["riotIdGameName"] + "#" + entry["riotIdTagline"], entry, entry["individualPosition"])
            user.load_stats()
            self.players.append(user)
            
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