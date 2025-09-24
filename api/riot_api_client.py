import requests
import json
class MatchRequestException(Exception):
    pass
class AccountRequestException(Exception):
    pass
class MatchesRequestException(Exception):
    pass
class ChampMasteryRequestException(Exception):
    pass
class RiotClient:
    def __init__(self, api_key, user, tag):
        self.api_key = api_key
        self.api_headers = {
            "X-Riot-Token": self.api_key
            }
        self.user = user
        self.tag = tag
        self.match_url = "https://americas.api.riotgames.com/lol/match/v5/matches/"
        self.acc_url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{self.user}/{self.tag}"

    def get_match_data(self,match_id):
        response = requests.get(self.match_url+match_id, headers=self.api_headers)
        if(response.status_code != 200):
            raise MatchRequestException(f"API Error in get_match_data(): {response.status_code}")
        return response.json()
    def get_account_data(self):
        response = requests.get(self.acc_url, headers=self.api_headers)
        if(response.status_code != 200):
            raise AccountRequestException(f"API Error in get_account_data(): {response.status_code}")
        return response.json()
    def get_matches_data(self, puuid):
        matches_url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids"
        response = requests.get(matches_url, headers=self.api_headers)
        if(response.status_code != 200):
            raise MatchesRequestException(f"API Error in get_matches_data(): {response.status_code}")
        return response.json()
    def get_champ_mastery_data(self,puuid):
        url = f"https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}"
        response = requests.get(url, headers=self.api_headers)
        if(response.status_code != 200):
            raise ChampMasteryRequestException(f"API Error in get_champ_mastery(): {response.status_code}")
        return response.json()
