# Generated by Django 4.0.1 on 2022-01-31 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='팀 명')),
                ('homepage', models.CharField(blank=True, max_length=50, verbose_name='홈페이지 주소')),
                ('youtube', models.CharField(blank=True, max_length=50, verbose_name='유튜브 주소')),
            ],
            options={
                'verbose_name': '축구 팀',
                'verbose_name_plural': '축구 팀',
            },
        ),
    ]