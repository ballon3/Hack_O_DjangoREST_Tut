# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 22:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example_app', '0002_auto_20170128_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='song_title',
            field=models.CharField(default='', max_length=255),
        ),
    ]
