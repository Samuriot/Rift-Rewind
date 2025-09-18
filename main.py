from functions import champion as c, get_acc as r, match_game as m

from dotenv import load_dotenv
import os
import json

load_dotenv()
api_key = os.getenv("RIOT_API")

if __name__ == "__main__":
    user = input()
    tag = input()

    temp = r.Riot_Acc(api_key, user, tag)
    temp2 = temp.parse_matches_ids()
    for key, val in temp2.items():
        print(f"{key}: {val}")
    # match_test.print_basic_stats()