# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 19:12
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20170509_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='player_team',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='player_league', chained_model_field='player_league', null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Team'),
        ),
    ]
