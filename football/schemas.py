from ninja import Schema


class TeamIn(Schema):
    league_id: int = ''
    name: str
    homepage: str = ''
    youtube: str = ''

class TeamOut(Schema):
    name: str
    homepage: str
    description: str
    league_name: str

class LeagueIn(Schema):
    name: str
    country: str
    ranking_in_country: int = 1

class LeagueOut(Schema):
    name: str
    country: str
    ranking_in_country: int
    description: str
