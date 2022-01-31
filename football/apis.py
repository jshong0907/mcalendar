from typing import List

from ninja import Router

from django.shortcuts import get_object_or_404

from football.models import Team
from football.schemas import TeamIn
from football.schemas import TeamOut

router = Router()

@router.post('/', response=TeamOut)
def create_team(request, data: TeamIn):
    """축구 팀 등록 API"""
    return Team.objects.create(
        **dict(data),
    )

@router.get('/', response=List[TeamOut])
def list_team(request):
    """축구 팀 리스트"""
    return Team.objects.all()

@router.get('/{team_id}', response=TeamOut)
def retrieve_team(request, team_id: int):
    """축구 팀 가져오기"""
    return get_object_or_404(Team, id=team_id)
