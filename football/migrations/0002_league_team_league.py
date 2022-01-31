# Generated by Django 4.0.1 on 2022-01-31 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='리그 명')),
                ('country', models.CharField(max_length=50, verbose_name='소속 국가')),
                ('ranking_in_country', models.PositiveSmallIntegerField(verbose_name='자국내 리그 순위')),
            ],
            options={
                'verbose_name': '축구 리그',
                'verbose_name_plural': '축구 리그',
            },
        ),
        migrations.AddField(
            model_name='team',
            name='league',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='teams', to='football.league', verbose_name='소속 리그'),
            preserve_default=False,
        ),
    ]