from django.db import models


class Continent(models.Model):
    """대륙"""
    name = models.CharField(
        verbose_name='대륙명',
        max_length=50,
        unique=True,
    )
    english_name = models.CharField(
        verbose_name='대륙 영문명',
        max_length=50,
        unique=True,
    )

    class Meta:
        verbose_name = '대륙'
        verbose_name_plural = '대륙'

    def __str__(self) -> str:
        return f'[대륙 {self.id}] {self.name}'


class Country(models.Model):
    """국가"""
    name = models.CharField(
        verbose_name='국가명',
        max_length=50,
        unique=True,
    )
    english_name = models.CharField(
        verbose_name='국가 영문명',
        max_length=50,
        unique=True,
    )
    continent = models.ForeignKey(
        'countries.Continent',
        on_delete=models.PROTECT,
        related_name='countries',
        verbose_name='대륙',
    )

    class Meta:
        verbose_name = '국가'
        verbose_name_plural = '국가'

    def __str__(self) -> str:
        return f'[국가 {self.id}] {self.name}'

    @property
    def continent_name(self) -> str:
        """대륙명"""
        return self.continent.name
