from django.db import models

class Team(models.Model):
    """프로 축구 대회 팀"""
    name = models.CharField(
        '팀 명',
        max_length=30,
    )
    homepage = models.CharField(
        '홈페이지 주소',
        max_length=50,
        blank=True,
    )
    youtube = models.CharField(
        '유튜브 주소',
        max_length=50,
        blank=True,
    )

    class Meta:
        verbose_name = '축구 팀'
        verbose_name_plural = '축구 팀'

    def __str__(self):
        return f'[축구 팀 {self.id}] {self.name}'

    @property
    def description(self):
        return str(self)