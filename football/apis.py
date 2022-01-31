from typing import List

from ninja import Router

from django.shortcuts import get_object_or_404

from football.models import Team
from football.models import League
from football.schemas import TeamIn
from football.schemas import TeamOut
from football.schemas import LeagueIn
from football.schemas import LeagueOut

router = Router()

@router.post('/team/', response=TeamOut)
def create_team(request, data: TeamIn):
    """축구 팀 등록"""
    return Team.objects.create(
        **data.dict(),
    )

@router.get('/team/', response=List[TeamOut])
def list_team(request):
    """축구 팀 리스트"""
    return Team.objects.all()

@router.get('/team/{team_id}', response=TeamOut)
def retrieve_team(request, team_id: int):
    """축구 팀 가져오기"""
    return get_object_or_404(Team, id=team_id)

@router.post('/league/', response=LeagueOut)
def create_league(request, data: LeagueIn):
    """축구 리그 등록"""
    return League.objects.create(
        **data.dict(),
    )
