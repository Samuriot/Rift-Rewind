from abc import ABC, abstractmethod
import json

class Performance(ABC):
    @abstractmethod
    def load_stats(self):
        pass

class EconomyPerformance(Performance):
    def __init__(self, json_file):
        self.json_file = json_file
        self.load_stats()
    
    def load_stats(self):
        self.goldEarned = self.json_file["goldEarned"]
        self.goldSpent = self.json_file["goldSpent"]
        self.totalMinionsKilled = self.json_file["totalMinionsKilled"]
        self.neutralMinionsKilled = self.json_file["neutralMinionsKilled"]
        self.totalMinionsKilled = self.json_file["totalMinionsKilled"]
        self.totalHeal = self.json_file["totalHeal"]
        self.totalUnitsHealed = self.json_file["totalUnitsHealed"]
        
    def get_gold(self):
        return {
            "earned": self.goldEarned,
            "spent": self.goldSpent
        }
    
    def get_cs(self):
        return {
            "total": self.totalMinionsKilled,
            "neutral": self.neutralMinionsKilled
        }
    
    def get_healing(self):
        return {
            "totalHeal": self.totalHeal,
            "totalUnitsHealed": self.totalUnitsHealed
        }

class CombatPerformance(Performance):
    def __init__(self, json_file):
        self.json_file = json_file
        self.load_stats()
    
    def load_stats(self):
        self.kills = self.json_file["kills"]
        self.deaths = self.json_file["deaths"]
        self.assists = self.json_file["assists"]
        if self.deaths != 0:
            self.kda = round((self.kills + self.assists) / self.deaths, 3)
        else:
            self.kda = self.kills + self.assists

        self.damageDealtToChampions = self.json_file["totalDamageDealtToChampions"]
        self.damageDealtToObjectives = self.json_file["damageDealtToObjectives"]
        self.damageDealtToTurrets = self.json_file["damageDealtToTurrets"]
        self.totalDamageTaken = self.json_file["totalDamageTaken"]
        self.physicalDamageTaken = self.json_file["physicalDamageTaken"]
        self.magicDamageTaken = self.json_file["magicDamageTaken"]
        self.trueDamageTaken = self.json_file["trueDamageTaken"]
        self.wardsPlaced = self.json_file["wardsPlaced"]
        self.wardsKilled = self.json_file["wardsKilled"]
        self.visionWardsBoughtInGame = self.json_file["visionWardsBoughtInGame"]
        
    def get_damage_dealt(self):
        return {
            "toChampions": self.damageDealtToChampions,
            "toObjectives": self.damageDealtToObjectives,
            "toTurrets": self.damageDealtToTurrets
        }
    
    def get_damage_taken(self):
        return {
            "total": self.totalDamageTaken,
            "physical": self.physicalDamageTaken,
            "magic": self.magicDamageTaken,
            "true": self.trueDamageTaken
        }    
    def get_vision(self):
        return {
            "wardsPlaced": self.wardsPlaced,
            "wardsKilled": self.wardsKilled,
            "visionWardsBoughtInGame": self.visionWardsBoughtInGame
        }
    
    def get_cc_time(self):
        return self.timeEnemySpentControlled


# Player_Performance class which represents an individual's performance across a game of LoL
# used by Riot_Acc and Match_Game classes via composition
class Player_Performance(Performance):
    # __init__ constructor
    def __init__(self, id, user, dump, role):
        self.id = id
        self.user = user
        self.json_file = dump
        self.role = self.get_role(role)
        self.load_stats()
        self.champion = self.json_file["championId"]
        
    # load_stats method will parse self.json_file for information from Riot API
    # TODO: WIP currently, need to add more areas to parse
    def load_stats(self):
        self.combat_performance = CombatPerformance(self.json_file)
        self.economy_performance = EconomyPerformance(self.json_file)
    
    # __str__ getter method
    def __str__(self):
        return json.dumps(self.json_file, indent=4)
    
    # getter methods for member data
    def get_KDA(self):
        return f"{self.kills}/{self.deaths}/{self.assists} - {self.kda}"
    
    def get_kills(self):
        return self.kills
    
    def get_deaths(self):
        return self.deaths
    
    def get_assists(self):
        return self.assists
    
    def get_role(self, role):
        if role.lower() != "invalid":
            return role
        else:
            return "ARAM"

