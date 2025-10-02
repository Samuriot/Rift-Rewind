from pydantic import BaseModel
from typing import List, Optional


class LolMatchV5MatchMetadata(BaseModel):
    dataVersion: str
    matchId: str
    participants: List[str]


class LolMatchV5MatchTeamObjective(BaseModel):
    first: bool
    kills: int


class LolMatchV5MatchInfoParticipantChallenges(BaseModel):
    # all fields optional because of total=False in TypedDict
    # (keep same name to match API keys)
    _12AssistStreakCount: Optional[int] = None
    abilityUses: Optional[int] = None
    acesBefore15Minutes: Optional[int] = None
    alliedJungleMonsterKills: Optional[int] = None
    baronTakedowns: Optional[int] = None
    blastConeOppositeOpponentCount: Optional[int] = None
    bountyGold: Optional[float] = None
    buffsStolen: Optional[int] = None
    completeSupportQuestInTime: Optional[int] = None
    controlWardTimeCoverageInRiverOrEnemyHalf: Optional[float] = None
    controlWardsPlaced: Optional[int] = None
    damagePerMinute: Optional[float] = None
    damageTakenOnTeamPercentage: Optional[float] = None
    dancedWithRiftHerald: Optional[int] = None
    deathsByEnemyChamps: Optional[int] = None
    dodgeSkillShotsSmallWindow: Optional[int] = None
    doubleAces: Optional[int] = None
    dragonTakedowns: Optional[int] = None
    earliestBaron: Optional[float] = None
    earliestElderDragon: Optional[float] = None
    earlyLaningPhaseGoldExpAdvantage: Optional[int] = None
    effectiveHealAndShielding: Optional[float] = None
    elderDragonKillsWithOpposingSoul: Optional[int] = None
    elderDragonMultikills: Optional[int] = None
    enemyChampionImmobilizations: Optional[int] = None
    enemyJungleMonsterKills: Optional[int] = None
    epicMonsterKillsNearEnemyJungler: Optional[int] = None
    epicMonsterKillsWithin30SecondsOfSpawn: Optional[int] = None
    epicMonsterSteals: Optional[int] = None
    epicMonsterStolenWithoutSmite: Optional[int] = None
    firstTurretKilled: Optional[int] = None
    firstTurretKilledTime: Optional[float] = None
    flawlessAces: Optional[int] = None
    fullTeamTakedown: Optional[int] = None
    gameLength: Optional[float] = None
    getTakedownsInAllLanesEarlyJungleAsLaner: Optional[int] = None
    goldPerMinute: Optional[float] = None
    hadOpenNexus: Optional[int] = None
    immobilizeAndKillWithAlly: Optional[int] = None
    initialBuffCount: Optional[int] = None
    initialCrabCount: Optional[int] = None
    jungleCsBefore10Minutes: Optional[float] = None
    junglerTakedownsNearDamagedEpicMonster: Optional[int] = None
    kTurretsDestroyedBeforePlatesFall: Optional[int] = None
    kda: Optional[float] = None
    killAfterHiddenWithAlly: Optional[int] = None
    killParticipation: Optional[float] = None
    killedChampTookFullTeamDamageSurvived: Optional[int] = None
    killingSprees: Optional[int] = None
    killsNearEnemyTurret: Optional[int] = None
    killsOnOtherLanesEarlyJungleAsLaner: Optional[int] = None
    killsOnRecentlyHealedByAramPack: Optional[int] = None
    killsUnderOwnTurret: Optional[int] = None
    killsWithHelpFromEpicMonster: Optional[int] = None
    knockEnemyIntoTeamAndKill: Optional[int] = None
    landSkillShotsEarlyGame: Optional[int] = None
    laneMinionsFirst10Minutes: Optional[int] = None
    laningPhaseGoldExpAdvantage: Optional[int] = None
    legendaryCount: Optional[int] = None
    lostAnInhibitor: Optional[int] = None
    maxCsAdvantageOnLaneOpponent: Optional[float] = None
    maxKillDeficit: Optional[int] = None
    maxLevelLeadLaneOpponent: Optional[int] = None
    mejaisFullStackInTime: Optional[int] = None
    moreEnemyJungleThanOpponent: Optional[float] = None
    multiKillOneSpell: Optional[int] = None
    multiTurretRiftHeraldCount: Optional[int] = None
    multikills: Optional[int] = None
    multikillsAfterAggressiveFlash: Optional[int] = None
    mythicItemUsed: Optional[int] = None
    outerTurretExecutesBefore10Minutes: Optional[int] = None
    outnumberedKills: Optional[int] = None
    outnumberedNexusKill: Optional[int] = None
    perfectDragonSoulsTaken: Optional[int] = None
    perfectGame: Optional[int] = None
    pickKillWithAlly: Optional[int] = None
    playedChampSelectPosition: Optional[int] = None
    poroExplosions: Optional[int] = None
    quickCleanse: Optional[int] = None
    quickFirstTurret: Optional[int] = None
    quickSoloKills: Optional[int] = None
    riftHeraldTakedowns: Optional[int] = None
    saveAllyFromDeath: Optional[int] = None
    scuttleCrabKills: Optional[int] = None
    shortestTimeToAceFromFirstTakedown: Optional[float] = None
    skillshotsDodged: Optional[int] = None
    skillshotsHit: Optional[int] = None
    snowballsHit: Optional[int] = None
    soloBaronKills: Optional[int] = None
    soloKills: Optional[int] = None
    stealthWardsPlaced: Optional[int] = None
    survivedSingleDigitHpCount: Optional[int] = None
    survivedThreeImmobilizesInFight: Optional[int] = None
    takedownOnFirstTurret: Optional[int] = None
    takedowns: Optional[int] = None
    takedownsAfterGainingLevelAdvantage: Optional[int] = None
    takedownsBeforeJungleMinionSpawn: Optional[int] = None
    takedownsFirstXMinutes: Optional[int] = None
    takedownsInAlcove: Optional[int] = None
    takedownsInEnemyFountain: Optional[int] = None
    teamBaronKills: Optional[int] = None
    teamDamagePercentage: Optional[float] = None
    teamElderDragonKills: Optional[int] = None
    teamRiftHeraldKills: Optional[int] = None
    tookLargeDamageSurvived: Optional[int] = None
    turretPlatesTaken: Optional[int] = None
    turretTakedowns: Optional[int] = None
    turretsTakenWithRiftHerald: Optional[int] = None
    twentyMinionsIn3SecondsCount: Optional[int] = None
    twoWardsOneSweeperCount: Optional[int] = None
    unseenRecalls: Optional[int] = None
    visionScoreAdvantageLaneOpponent: Optional[float] = None
    visionScorePerMinute: Optional[float] = None
    wardTakedowns: Optional[int] = None
    wardTakedownsBefore20M: Optional[int] = None
    wardsGuarded: Optional[int] = None
    earliestDragonTakedown: Optional[float] = None
    baronBuffGoldAdvantageOverThreshold: Optional[int] = None
    teleportTakedowns: Optional[int] = None
    fastestLegendary: Optional[float] = None
    highestChampionDamage: Optional[int] = None
    highestCrowdControlScore: Optional[int] = None
    junglerKillsEarlyJungle: Optional[int] = None
    killsOnLanersEarlyJungleAsJungler: Optional[int] = None
    fasterSupportQuestCompletion: Optional[int] = None
    highestWardKills: Optional[int] = None
    soloTurretsLategame: Optional[int] = None
    thirdInhibitorDestroyedTime: Optional[float] = None
    HealFromMapSources: Optional[float] = None
    InfernalScalePickup: Optional[int] = None
    SWARM_DefeatAatrox: Optional[int] = None
    SWARM_DefeatBriar: Optional[int] = None
    SWARM_DefeatMiniBosses: Optional[int] = None
    SWARM_EvolveWeapon: Optional[int] = None
    SWARM_Have3Passives: Optional[int] = None
    SWARM_KillEnemy: Optional[int] = None
    SWARM_PickupGold: Optional[int] = None
    SWARM_ReachLevel50: Optional[int] = None
    SWARM_Survive15Min: Optional[int] = None
    SWARM_WinWith5EvolvedWeapons: Optional[int] = None
    fistBumpParticipation: Optional[int] = None
    legendaryItemUsed: Optional[List[int]] = None
    voidMonsterKill: Optional[int] = None


class LolMatchV5MatchInfoParticipantPerksStatPerks(BaseModel):
    defense: int
    flex: int
    offense: int


class LolMatchV5MatchInfoParticipantPerksStyleSelection(BaseModel):
    perk: int
    var1: int
    var2: int
    var3: int


class LolMatchV5MatchInfoParticipantPerksStyle(BaseModel):
    description: str
    selections: List[LolMatchV5MatchInfoParticipantPerksStyleSelection]
    style: int


class LolMatchV5MatchInfoParticipantPerks(BaseModel):
    statPerks: LolMatchV5MatchInfoParticipantPerksStatPerks
    styles: List[LolMatchV5MatchInfoParticipantPerksStyle]


class LolMatchV5MatchInfoParticipantMissions(BaseModel):
    playerScore0: float
    playerScore1: float
    playerScore10: float
    playerScore11: float
    playerScore2: float
    playerScore3: float
    playerScore4: float
    playerScore5: float
    playerScore6: float
    playerScore7: float
    playerScore8: float
    playerScore9: float


class LolMatchV5MatchInfoParticipant(BaseModel):
    allInPings: int
    assistMePings: int
    assists: int
    baitPings: Optional[int] = None
    baronKills: int
    basicPings: int
    bountyLevel: Optional[int] = None
    challenges: Optional[LolMatchV5MatchInfoParticipantChallenges] = None
    champExperience: int
    champLevel: int
    championId: int
    championName: str
    championTransform: int
    commandPings: int
    consumablesPurchased: int
    damageDealtToBuildings: int
    damageDealtToObjectives: int
    damageDealtToTurrets: int
    damageSelfMitigated: int
    dangerPings: int
    deaths: int
    detectorWardsPlaced: int
    doubleKills: int
    dragonKills: int
    eligibleForProgression: bool
    enemyMissingPings: int
    enemyVisionPings: int
    firstBloodAssist: bool
    firstBloodKill: bool
    firstTowerAssist: bool
    firstTowerKill: bool
    gameEndedInEarlySurrender: bool
    gameEndedInSurrender: bool
    getBackPings: int
    goldEarned: int
    goldSpent: int
    holdPings: int
    individualPosition: str
    inhibitorKills: int
    inhibitorTakedowns: int
    inhibitorsLost: int
    item0: int
    item1: int
    item2: int
    item3: int
    item4: int
    item5: int
    item6: int
    itemsPurchased: int
    killingSprees: int
    kills: int
    lane: str
    largestCriticalStrike: int
    largestKillingSpree: int
    largestMultiKill: int
    longestTimeSpentLiving: int
    magicDamageDealt: int
    magicDamageDealtToChampions: int
    magicDamageTaken: int
    missions: LolMatchV5MatchInfoParticipantMissions
    needVisionPings: int
    neutralMinionsKilled: int
    nexusKills: int
    nexusLost: int
    nexusTakedowns: int
    objectivesStolen: int
    objectivesStolenAssists: int
    onMyWayPings: int
    participantId: int
    pentaKills: int
    perks: LolMatchV5MatchInfoParticipantPerks
    physicalDamageDealt: int
    physicalDamageDealtToChampions: int
    physicalDamageTaken: int
    placement: int
    playerAugment1: int
    playerAugment2: int
    playerAugment3: int
    playerAugment4: int
    playerAugment5: int
    playerAugment6: int
    playerSubteamId: int
    PlayerScore0: Optional[float] = None
    PlayerScore1: Optional[float] = None
    PlayerScore10: Optional[float] = None
    PlayerScore11: Optional[float] = None
    PlayerScore2: Optional[float] = None
    PlayerScore3: Optional[float] = None
    PlayerScore4: Optional[float] = None
    PlayerScore5: Optional[float] = None
    PlayerScore6: Optional[float] = None
    PlayerScore7: Optional[float] = None
    PlayerScore8: Optional[float] = None
    PlayerScore9: Optional[float] = None
    profileIcon: int
    pushPings: int
    puuid: str
    quadraKills: int
    riotIdTagline: str
    riotIdGameName: str
    role: str
    sightWardsBoughtInGame: int
    spell1Casts: int
    spell2Casts: int
    spell3Casts: int
    spell4Casts: int
    subteamPlacement: int
    summoner1Casts: int
    summoner1Id: int
    summoner2Casts: int
    summoner2Id: int
    summonerId: str
    summonerLevel: int
    summonerName: Optional[str] = None
    teamEarlySurrendered: bool
    teamId: int
    teamPosition: str
    timeCCingOthers: int
    timePlayed: int
    totalAllyJungleMinionsKilled: int
    totalDamageDealt: int
    totalDamageDealtToChampions: int
    totalDamageShieldedOnTeammates: int
    totalDamageTaken: int
    totalEnemyJungleMinionsKilled: int
    totalHeal: int
    totalHealsOnTeammates: int
    totalMinionsKilled: int
    totalTimeCCDealt: int
    totalTimeSpentDead: int
    totalUnitsHealed: int
    tripleKills: int
    trueDamageDealt: int
    trueDamageDealtToChampions: int
    trueDamageTaken: int
    turretKills: int
    turretTakedowns: int
    turretsLost: int
    unrealKills: int
    visionClearedPings: int
    visionScore: int
    visionWardsBoughtInGame: int
    wardsKilled: int
    wardsPlaced: int
    retreatPings: Optional[int] = None
    win: bool


class LolMatchV5MatchInfoTeamBan(BaseModel):
    championId: int
    pickTurn: int


class LolMatchV5MatchInfoTeamObjectives(BaseModel):
    baron: LolMatchV5MatchTeamObjective
    champion: LolMatchV5MatchTeamObjective
    dragon: LolMatchV5MatchTeamObjective
    atakhan: Optional[LolMatchV5MatchTeamObjective] = None
    horde: LolMatchV5MatchTeamObjective
    inhibitor: LolMatchV5MatchTeamObjective
    riftHerald: LolMatchV5MatchTeamObjective
    tower: LolMatchV5MatchTeamObjective


class LolMatchV5MatchInfoTeamFeatState(BaseModel):
    featState: int


class LolMatchV5MatchInfoTeamFeats(BaseModel):
    EPIC_MONSTER_KILL: LolMatchV5MatchInfoTeamFeatState
    FIRST_BLOOD: LolMatchV5MatchInfoTeamFeatState
    FIRST_TURRET: LolMatchV5MatchInfoTeamFeatState


class LolMatchV5MatchInfoTeam(BaseModel):
    bans: List[LolMatchV5MatchInfoTeamBan]
    objectives: LolMatchV5MatchInfoTeamObjectives
    teamId: int
    win: bool
    feats: Optional[LolMatchV5MatchInfoTeamFeats] = None


class LolMatchV5MatchInfo(BaseModel):
    gameCreation: int
    gameDuration: int
    gameEndTimestamp: int
    gameId: int
    gameMode: str
    gameName: str
    gameStartTimestamp: int
    gameType: str
    gameVersion: str
    mapId: int
    participants: List[LolMatchV5MatchInfoParticipant]
    platformId: str
    queueId: int
    teams: List[LolMatchV5MatchInfoTeam]
    tournamentCode: str
    endOfGameResult: str


class LolMatchV5Match(BaseModel):
    metadata: LolMatchV5MatchMetadata
    info: LolMatchV5MatchInfo
