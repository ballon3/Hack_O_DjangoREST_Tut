# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('artist_name', models.CharField(default='', max_length=255)),
                ('song_year', models.IntegerField(blank=True, null=True)),
                ('song_lyrics', models.TextField()),
            ],
            options={
                'db_table': 'song_lyrics',
            },
        ),
    ]
