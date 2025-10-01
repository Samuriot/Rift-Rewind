class AccountV1Account:
    puuid: str
    gameName: str
    tagLine: str

    def __init__(self, puuid: str, gameName: str, tagLine: str):
        self.puuid = puuid
        self.gameName = gameName
        self.tagLine = tagLine


class AccountV1ActiveShard:
    puuid: str
    game: str
    activeShard: str

    def __init__(self, puuid: str, game: str, activeShard: str):
        self.puuid = puuid
        self.game = game
        self.activeShard = activeShard
