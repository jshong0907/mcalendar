from tabnanny import verbose
from django.db import models

class Team(models.Model):
    """프로 축구 대회 팀"""
    name = models.CharField(
        verbose_name='팀 명',
        max_length=30,
    )
    homepage = models.CharField(
        verbose_name='홈페이지 주소',
        max_length=50,
        blank=True,
    )
    youtube = models.CharField(
        verbose_name='유튜브 주소',
        max_length=50,
        blank=True,
    )
    league = models.ForeignKey(
        'football.League',
        related_name='teams',
        on_delete=models.PROTECT,
        verbose_name='소속 리그',
    )

    class Meta:
        verbose_name = '축구 팀'
        verbose_name_plural = '축구 팀'

    def __str__(self):
        return f'[축구 팀 {self.id}] {self.name}'

    @property
    def description(self) -> str:
        """설명"""
        return str(self)

    @property
    def league_name(self) -> str:
        """리그 명"""
        return self.league.name


class League(models.Model):
    """축구 리그"""
    name = models.CharField(
        verbose_name='리그 명',
        max_length=50,
    )
    country = models.CharField(
        verbose_name='소속 국가',
        max_length=50,
    )
    ranking_in_country = models.PositiveSmallIntegerField(
        verbose_name='자국내 리그 순위',
    )

    class Meta:
        verbose_name = '축구 리그'
        verbose_name_plural = '축구 리그'

    def __str__(self):
        return f'[축구 리그 {self.id}] {self.name}'

    @property
    def description(self) -> str:
        """설명"""
        return str(self)
