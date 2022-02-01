from typing import List

from ninja import Router
from django.shortcuts import get_object_or_404

from countries.schemas import CountryOut
from countries.selectors import filter_countries
from countries.models import Country


router = Router(tags=['국가'])

@router.get('/', response=List[CountryOut])
def list_countries(request, continent_name: str = None):
    """국가 목록 조회 API
    
    continent_name을 통하여 필터링한다.
    continent_name가 없다면 전체 국가 목록을 반환한다.
    """
    return filter_countries(continent_name=continent_name)


@router.get('/{country_id}/', response=CountryOut)
def get_country(request, country_id: str):
    """국가 정보 조회 API"""
    return get_object_or_404(Country, id=country_id)
