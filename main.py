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
    match_history = temp.parse_matches_ids()
    # print("{")
    # for key, val in match_history.items():
    #     print(f"\"{key}\": {val},")
    # print("}")
    temp.compile_match_stats()
    # match_test.print_basic_stats()