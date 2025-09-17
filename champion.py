import requests
import json

class Champion:
    def __init__(self, id, name, title, blurb, info, tags, partype, stats):
        self.id = id
        self.name = name
        self.title = title
        self.description = blurb
        self.info = info
        self.tags = tags
        self.partype = partype
        self.stats = stats
        self.image_url = f"https://ddragon.leagueoflegends.com/cdn/15.18.1/img/champion/{self.name}.png"

    
    def __str__(self):
        return self.name

def create_champ_list():
    url = "https://ddragon.leagueoflegends.com/cdn/15.18.1/data/en_US/champion.json"
    champ_list = requests.get(url)
    if(champ_list.status_code != 200):
            raise Exception(f"API Error in create_champ_list: {champ_list.status_code}")
    champ_list = json.loads(champ_list.text)
    all_champs = {}

    for champion, desc in champ_list['data'].items():
        all_champs[desc["key"]] = Champion(desc["key"], desc["name"], desc["title"], desc["blurb"], desc["info"], desc["tags"], desc["partype"], desc["stats"])
    
    return all_champs

