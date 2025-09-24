from abc import ABC, abstractmethod
import json

class Performance(ABC):
    @abstractmethod
    def load_stats(self):
        pass
    
class EconomyPerformance(Performance):
    def __init__(self, match_data):
        self.match_data = match_data
        self.load_stats()
    
    def load_stats(self):
        self.goldEarned = self.match_data["goldEarned"]
        self.goldSpent = self.match_data["goldSpent"]
        self.totalMinionsKilled = self.match_data["totalMinionsKilled"]
        self.neutralMinionsKilled = self.match_data["neutralMinionsKilled"]
        self.totalHeal = self.match_data["totalHeal"]
        self.totalUnitsHealed = self.match_data["totalUnitsHealed"]
        self.goldPerMin = self.match_data["challenges"]["goldPerMinute"]
        
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
    def __init__(self, match_data):
        self.match_data = match_data
        self.load_stats()
    
    def load_stats(self):
        self.kills = self.match_data["kills"]
        self.deaths = self.match_data["deaths"]
        self.assists = self.match_data["assists"]
        if self.deaths != 0:
            self.kda = round((self.kills + self.assists) / self.deaths, 3)
        else:
            self.kda = self.kills + self.assists

        self.damageDealtToChampions = self.match_data["totalDamageDealtToChampions"]
        self.damageDealtToObjectives = self.match_data["damageDealtToObjectives"]
        self.damageDealtToTurrets = self.match_data["damageDealtToTurrets"]
        self.totalDamageTaken = self.match_data["totalDamageTaken"]
        self.physicalDamageTaken = self.match_data["physicalDamageTaken"]
        self.magicDamageTaken = self.match_data["magicDamageTaken"]
        self.trueDamageTaken = self.match_data["trueDamageTaken"]
        self.wardsPlaced = self.match_data["wardsPlaced"]
        self.wardsKilled = self.match_data["wardsKilled"]
        self.visionWardsBoughtInGame = self.match_data["visionWardsBoughtInGame"]
        self.damagerPerMinute = self.match_data["challenges"]["damagePerMinute"]
        self.percentDamageTaken = self.match_data["challenges"]["damageTakenOnTeamPercentage"]
        self.numEnemyChampCC = self.match_data["challenges"]["enemyChampionImmobilizations"]
        self.killWithAllyCC = self.match_data["challenges"]["immobilizeAndKillWithAlly"]
        
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
    def __init__(self, match_data):
        self.match_data = match_data
        self.load_stats()
    
    def load_stats(self):
        self.baronKills = self.match_data["baronKills"]
        self.challengesDict = self.match_data["challenges"]
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
        self.match_data = dump
        self.role = self.get_role(role)
        self.champion = self.match_data["championId"]
        self.load_stats()
        pass
        
    # load_stats method will parse self.match_data for information from Riot API
    # TODO: WIP currently, need to add more areas to parse
    def load_stats(self):
        self.combat_performance = CombatPerformance(self.match_data)
        self.economy_performance = EconomyPerformance(self.match_data)
        self.objective_performance = ObjectivePerformance(self.match_data)
    
    # __str__ getter method
    def __str__(self):
        return json.dumps(self.match_data, indent=4)
    
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

