from typing import List, Dict, Optional
from pydantic import BaseModel


class LolMatchV5MatchTimelineParticipantFrameChampionStats(BaseModel):
    abilityHaste: int
    abilityPower: int
    armor: int
    armorPen: int
    armorPenPercent: int
    attackDamage: int
    attackSpeed: int
    bonusArmorPenPercent: int
    bonusMagicPenPercent: int
    ccReduction: int
    cooldownReduction: int
    health: int
    healthMax: int
    healthRegen: int
    lifesteal: int
    magicPen: int
    magicPenPercent: int
    magicResist: int
    movementSpeed: int
    omnivamp: int
    physicalVamp: int
    power: int
    powerMax: int
    powerRegen: int
    spellVamp: int


class LolMatchV5MatchTimelineParticipantFrameDamageStats(BaseModel):
    magicDamageDone: int
    magicDamageDoneToChampions: int
    magicDamageTaken: int
    physicalDamageDone: int
    physicalDamageDoneToChampions: int
    physicalDamageTaken: int
    totalDamageDone: int
    totalDamageDoneToChampions: int
    totalDamageTaken: int
    trueDamageDone: int
    trueDamageDoneToChampions: int
    trueDamageTaken: int


class LolMatchV5MatchTimelinePosition(BaseModel):
    x: int
    y: int


class LolMatchV5MatchTimelineParticipantFrame(BaseModel):
    championStats: LolMatchV5MatchTimelineParticipantFrameChampionStats
    currentGold: int
    damageStats: LolMatchV5MatchTimelineParticipantFrameDamageStats
    goldPerSecond: int
    jungleMinionsKilled: int
    level: int
    minionsKilled: int
    participantId: int
    position: LolMatchV5MatchTimelinePosition
    timeEnemySpentControlled: int
    totalGold: int
    xp: int


class LolMatchV5MatchTimelineEventDamage(BaseModel):
    basic: bool
    magicDamage: int
    name: str
    participantId: int
    physicalDamage: int
    spellName: str
    spellSlot: int
    trueDamage: int
    type: str


class LolMatchV5MatchTimelineMetadata(BaseModel):
    dataVersion: str
    matchId: str
    participants: List[str]


class LolMatchV5MatchTimelineInfoFrameEvent(BaseModel):
    afterId: Optional[int] = None
    beforeId: Optional[int] = None
    goldGain: Optional[int] = None
    participantId: Optional[int] = None
    timestamp: int
    type: str
    creatorId: Optional[int] = None
    wardType: Optional[str] = None
    level: Optional[int] = None
    itemId: Optional[int] = None
    assistingParticipantIds: Optional[List[int]] = None
    bounty: Optional[int] = None
    killStreakLength: Optional[int] = None
    killerId: Optional[int] = None
    position: Optional[LolMatchV5MatchTimelinePosition] = None
    shutdownBounty: Optional[int] = None
    victimDamageDealt: Optional[List[LolMatchV5MatchTimelineEventDamage]] = None
    victimDamageReceived: Optional[List[LolMatchV5MatchTimelineEventDamage]] = None
    victimId: Optional[int] = None
    levelUpType: Optional[str] = None
    skillSlot: Optional[int] = None
    realTimestamp: Optional[int] = None
    monsterType: Optional[str] = None
    monsterSubType: Optional[str] = None
    killerTeamId: Optional[int] = None
    buildingType: Optional[str] = None
    laneType: Optional[str] = None
    teamId: Optional[int] = None


class LolMatchV5MatchTimelineInfoFrame(BaseModel):
    events: List[LolMatchV5MatchTimelineInfoFrameEvent]
    participantFrames: Dict[str, LolMatchV5MatchTimelineParticipantFrame]
    timestamp: int


class LolMatchV5MatchTimelineInfoParticipants(BaseModel):
    participantId: int
    puuid: str


class LolMatchV5MatchTimelineInfo(BaseModel):
    frameInterval: int
    frames: List[LolMatchV5MatchTimelineInfoFrame]
    gameId: int
    participants: List[LolMatchV5MatchTimelineInfoParticipants]
    endOfGameResult: str


class LolMatchV5MatchTimeline(BaseModel):
    metadata: LolMatchV5MatchTimelineMetadata
    info: LolMatchV5MatchTimelineInfo
