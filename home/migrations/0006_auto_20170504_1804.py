# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 01:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20170504_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='player_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Team'),
        ),
        migrations.AlterField(
            model_name='team',
            name='record',
            field=models.CharField(blank=True, default='', max_length=55),
        ),
        migrations.AlterField(
            model_name='team',
            name='runs_scored',
            field=models.IntegerField(blank=True, default='0'),
        ),
    ]
