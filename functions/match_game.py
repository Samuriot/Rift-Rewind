import requests
import json

match_url  = "https://americas.api.riotgames.com/lol/match/v5/matches/"

class Player:
    def __init__(self, id, user, dump, role):
        self.id = id
        self.user = user
        self.json_file = dump
        self.role = role
        
    def set_json_stats(self, json_file):
        self.json_file = json_file
    
    def __str__(self):
        return self.user

class Match_Game:
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
    
    def load_players(self):
        gameData = self.json_resp["info"]["participants"]
        for entry in gameData:
            user = Player(entry["puuid"], entry["riotIdGameName"] + "#" + entry["riotIdTagline"], entry, entry["individualPosition"])
            print(user.user + ": " + user.role)
            self.players.append(user)
            
            
    def print_details(self):
        print(json.dumps(self.json_resp, indent=4))