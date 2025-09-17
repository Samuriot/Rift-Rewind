from functions import champion as c, get_acc as r, match_game as m

from dotenv import load_dotenv
import requests
import json
import os

load_dotenv()
api_key = os.getenv("RIOT_API")

if __name__ == "__main__":
    user = input("please input your user: ")
    tag = input("please input your tag: ")

    temp = r.Riot_Acc(api_key, user, tag)
    print(temp.get_puuid())
    matches = temp.get_matches()
    match_test = m.Match_Game(api_key, matches[0])
    match_test.print_details()