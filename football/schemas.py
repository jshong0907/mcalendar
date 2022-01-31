from ninja import Schema


class TeamIn(Schema):
    name: str
    homepage: str = ''
    youtube: str = ''

class TeamOut(Schema):
    name: str
    homepage: str
    description: str
