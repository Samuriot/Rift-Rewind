import requests

class DataDragonItemRequestException(Exception):
    pass

class ItemDirectory:
    def __init__(self):
        self.items = self.create_item_list()

    def create_item_list(self):
        url = "https://ddragon.leagueoflegends.com/cdn/15.19.1/data/en_US/item.json"
        item_list = requests.get(url)
        if(item_list.status_code != 200):
                raise DataDragonItemRequestException(f"API Error in create_item_list: {item_list.status_code}")
        item_list = item_list.json()
        all_items = {}

        for item_id, desc in item_list['data'].items():
            into = desc["into"] if "into" in desc else []
            all_items[item_id] = Item(item_id, desc["name"], desc["description"], into, desc["gold"], desc["tags"], desc["stats"])
        return all_items

# Item class that contains basic information about a League item
class Item:
    # __init__ method to construct Champion object based on info from API
    def __init__(self, id, name, desc, into, gold, tags, stats):
        self.id = id
        self.name = name
        self.description = desc
        #NOTE: "into" is a list of item ids that this item builds into
        self.into = into
        self.gold = gold
        self.tags = tags
        self.stats = stats
        self.image_url = f"https://ddragon.leagueoflegends.com/cdn/15.19.1/img/item/{self.id}.png"
    # __str__ method to print an object properly
    def __str__(self):
        return self.name
