from typing import List

from django.db.models import Q

from countries.models import Country


def filter_countries(*, continent_name: str = None) -> List[Country]:
    query = Q(continent__name=continent_name) if continent_name is not None else Q()
    return Country.objects.filter(query)
