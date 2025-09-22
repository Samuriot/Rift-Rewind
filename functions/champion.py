# champion.py
# Defines the Champion class that hosts the information about LoL champions from Riot API

import requests
import json

class ChampionDirectory:
    def __init__(self):
        self.champions = self.create_champ_list()

    def create_champ_list(self):
        url = "https://ddragon.leagueoflegends.com/cdn/15.18.1/data/en_US/champion.json"
        champ_list = requests.get(url)
        if(champ_list.status_code != 200):
                raise Exception(f"API Error in create_champ_list: {champ_list.status_code}")
        champ_list = json.loads(champ_list.text)
        all_champs = {}

        for champion, desc in champ_list['data'].items():
            all_champs[desc["key"]] = Champion(desc["key"], desc["name"], desc["title"], desc["blurb"], desc["info"], desc["tags"], desc["partype"], desc["stats"])
        
        return all_champs
    
    def get_champ_main_tag(self, champ_id) -> str:
        if champ_id in self.champions:
            return self.champions[champ_id].main_tag
        
        return "None"


# Champion class that contains basic information about a League champ
class Champion:
    # __init__ method to construct Champion object based on info from API
    def __init__(self, id, name, title, blurb, info, tags, partype, stats):
        self.id = id
        self.name = name
        self.title = title
        self.description = blurb
        self.info = info
        self.tags = tags
        self.main_tag = tags[0] if len(tags) > 0 else "None"
        self.partype = partype
        self.stats = stats
        self.image_url = f"https://ddragon.leagueoflegends.com/cdn/15.18.1/img/champion/{self.name}.png"

    # __str__ method to print an object properly
    def __str__(self):
        return self.name

# create_champ_list will perform an API call to the DataDragon LoL API to get all champions
# will return a dictionary with the champ's ID as a key, and a Champion Object as the value


