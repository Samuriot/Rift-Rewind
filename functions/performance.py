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
        self.totalHeal = self.json_file["totalHeal"]
        self.totalUnitsHealed = self.json_file["totalUnitsHealed"]
        self.goldPerMin = self.json_file["challenges"]["goldPerMinute"]
        
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
        self.damagerPerMinute = self.json_file["challenges"]["damagePerMinute"]
        self.percentDamageTaken = self.json_file["challenges"]["damageTakenOnTeamPercentage"]
        self.numEnemyChampCC = self.json_file["challenges"]["enemyChampionImmobilizations"]
        self.killWithAllyCC = self.json_file["challenges"]["immobilizeAndKillWithAlly"]
        
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

class ObjectivePerformance(Performance):
    def __init__(self, json_file):
        self.json_file = json_file
        self.load_stats()
    
    def load_stats(self):
        self.baronKills = self.json_file["baronKills"]
        self.challengesDict = self.json_file["challenges"]
        # could potentially use this for something like: "You took advantage of Fire Dragon Soul By Picking Up x Scales"
        self.infernalScalePickups = self.challengesDict["InfernalScalePickup"]
        self.baronTakedowns = self.challengesDict["baronTakedowns"]
        self.blastConesOnEnemy = self.challengesDict["blastConeOppositeOpponentCount"]
        self.buffsStole = self.challengesDict["buffsStolen"]
        self.supportItemTimeComplete = self.challengesDict["completeSupportQuestInTime"]
        # self.controlWardUptimeInEnemyJg = self.challengesDict["controlWardTimeCoverageInRiverOrEnemyHalf"]
        self.numControlWards = self.challengesDict["controlWardsPlaced"]
        self.hardSkillShotsDodged = self.challengesDict["dodgeSkillShotsSmallWindow"]
        self.dragonTakedowns = self.challengesDict["dragonTakedowns"]
        # self.earliestDragKillTime = self.challengesDict["earliestDragonTakedown"]
        self.enemyJungleCampsStolen = self.challengesDict["enemyJungleMonsterKills"]
        self.killsAgainstElderDragBuff = self.challengesDict["elderDragonKillsWithOpposingSoul"]
        self.multiElderDragKills = self.challengesDict["elderDragonMultikills"]
        self.epicMonsterKillsNearEnemyJg = self.challengesDict["epicMonsterKillsNearEnemyJungler"]
        self.quickEpicMonsterKillsOnTempo = self.challengesDict["epicMonsterKillsWithin30SecondsOfSpawn"]
        self.epicMonsterSteals = self.challengesDict["epicMonsterSteals"]
        self.epicMonsterStealsNoSmite = self.challengesDict["epicMonsterStolenWithoutSmite"]
        self.firstTurretsKilled = self.challengesDict["firstTurretKilled"]
        self.flawlessAces = self.challengesDict["flawlessAces"]
        self.ace = self.challengesDict["fullTeamTakedown"]
        # self.earlyJgGankKills = self.challengesDict["getTakedownsInAllLanesEarlyJungleAsLaner"]
        self.hadOpenNexus = self.challengesDict["hadOpenNexus"]
        self.bronzeBushKills = self.challengesDict["killAfterHiddenWithAlly"]
        self.killsNearEnemyTurret = self.challengesDict["killsNearEnemyTurret"]
        self.killsUnderOwnTurret = self.challengesDict["killsUnderOwnTurret"]
        self.knockEnemyIntoTeamAndKill = self.challengesDict["knockEnemyIntoTeamAndKill"]
        self.landSkillShotsEarlyGame = self.challengesDict["landSkillShotsEarlyGame"]
        self.laneMinionsFirst10Minutes = self.challengesDict["laneMinionsFirst10Minutes"]
        # self.maxCsAdvantageOnLaner = self.challengesDict["maxCsAdvantageOnLaneOpponent"]
        self.maxKillDeficit = self.challengesDict["maxKillDeficit"]
        # self.maxLevelLeadLaneOpponent = self.challengesDict["maxLevelLeadLaneOpponent"]
        # idk what this means "in time"
        self.mejaisFullStackInTime = self.challengesDict["mejaisFullStackInTime"]
        self.multiKillOneSpell = self.challengesDict["multiKillOneSpell"]
        self.multiTurretRiftHeraldCount = self.challengesDict["multiTurretRiftHeraldCount"]
        self.multiKills = self.challengesDict["multikills"]
        self.multiKillsAfterFlash = self.challengesDict["multikillsAfterAggressiveFlash"]
        self.outnumberedKills = self.challengesDict["outnumberedKills"]
        self.picksWithAlly = self.challengesDict["pickKillWithAlly"]
        self.quickFirstTurret = self.challengesDict["quickFirstTurret"]
        self.quickSoloKills = self.challengesDict["quickSoloKills"]
        self.saveAllyFromDeath = self.challengesDict["saveAllyFromDeath"]
        self.scuttleCrabs = self.challengesDict["scuttleCrabKills"]
        self.numSkillshotDodged = self.challengesDict["skillshotsDodged"]
        self.numLandedSkillshot = self.challengesDict["skillshotsHit"]
        self.soloKills = self.challengesDict["soloKills"]
        self.survivedThreeCcInFight = self.challengesDict["survivedThreeImmobilizesInFight"]
        self.killsInAlcove = self.challengesDict["takedownsInAlcove"]
        self.killsInFountain = self.challengesDict["takedownsInEnemyFountain"]
        self.numTurretPlates = self.challengesDict["turretPlatesTaken"]
        self.numTurretsKilled = self.challengesDict["turretTakedowns"]
        self.numTurretsWithRiftHerald = self.challengesDict["turretsTakenWithRiftHerald"]
        self.numWardsKilled = self.challengesDict["wardTakedowns"]
    
    def get_nonzero_stats(self):
        self.nonzerolist = []
        for key, val in self.challengesDict.items():
            if val != 0:
                self.nonzerolist.append({key: val})

# Player_Performance class which represents an individual's performance across a game of LoL
# used by Riot_Acc and Match_Game classes via composition
class Player_Performance(Performance):
    # __init__ constructor
    def __init__(self, id, user, dump, role):
        self.id = id
        self.user = user
        self.json_file = dump
        self.role = self.get_role(role)
        self.champion = self.json_file["championId"]
        self.load_stats()
        pass
        
    # load_stats method will parse self.json_file for information from Riot API
    # TODO: WIP currently, need to add more areas to parse
    def load_stats(self):
        self.combat_performance = CombatPerformance(self.json_file)
        self.economy_performance = EconomyPerformance(self.json_file)
        self.objective_performance = ObjectivePerformance(self.json_file)
    
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

