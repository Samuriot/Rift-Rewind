from pydantic import BaseModel


class AccountV1Account(BaseModel):
    puuid: str
    gameName: str
    tagLine: str


class AccountV1ActiveShard(BaseModel):
    puuid: str
    game: str
    activeShard: str
