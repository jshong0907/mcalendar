from typing import List

from ninja import Router

from countries.schemas import CountryOut
from countries.selectors import filter_countries
from countries.models import Country


router = Router(tags=['국가'])

@router.get('/', response=List[CountryOut])
def list_countries(request, continent_name: str = None):
    return filter_countries(continent_name=continent_name)
