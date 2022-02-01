from ninja import Schema

class CountryOut(Schema):
    name: str
    english_name: str
    continent_name: str
