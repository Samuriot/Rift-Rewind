# match_game.py
# defines the Player_Performance and Match_Game classes which represent the data from
# a LoL game, as well as an individual player's performance based on a search

import json
# match_url global variable
match_url  = "https://americas.api.riotgames.com/lol/match/v5/matches/"
from api.performance import Player_Performance


# Match_Game Class, which represents an single LoL game, which should host the performance of each player
# based on an API call to the RIOT API, class will throw an exception will API call fails
class Match_Game:
    # load_players method which will go through each participant in the game & create a Player_Performance Object
    # optional method to be called, to prevent constantly call this method
    def load_players(self):
        gameData = self.match_data["info"]["participants"]
        for entry in gameData:
            user = Player_Performance(entry["puuid"], entry["riotIdGameName"] + "#" + entry["riotIdTagline"], entry, entry["individualPosition"])
            self.players.append(user)
    
    # __init__ constructor, which will throw an exception if Riot API fails        
    def __init__(self, riot_client, match_id):
        self.players = []
        self.riot_client = riot_client
        self.match_id = match_id
        self.match_data = self.riot_client.get_match_data(self.match_id)
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
        print(json.dumps(self.match_data, indent=4))