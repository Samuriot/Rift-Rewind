import requests
import json

match_url  = "https://americas.api.riotgames.com/lol/match/v5/matches/"
class Match_Game:
    def __init__(self, api_key, match_id):
        self.player_ids = []
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
    
    def print_details(self):
        print(json.dumps(self.json_resp, indent=4))