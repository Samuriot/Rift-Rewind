from api import champion as c, riot_api_client as rac

from dotenv import load_dotenv
import os
import json

from api.account import account as r

load_dotenv()
api_key = os.getenv("RIOT_API")

if __name__ == "__main__":
    user = input()
    tag = input()
    riot_client = rac.RiotClient(api_key, user, tag)
    temp = r.Riot_Acc(riot_client)
    match_history = temp.parse_matches_ids()
    temp.compile_match_stats()