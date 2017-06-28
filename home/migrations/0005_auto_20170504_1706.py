# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 00:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20170504_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='record',
            field=models.CharField(default='', max_length=55),
        ),
        migrations.AddField(
            model_name='team',
            name='runs_allowed',
            field=models.IntegerField(blank=True, default='0'),
        ),
        migrations.AddField(
            model_name='team',
            name='runs_scored',
            field=models.IntegerField(default='0'),
        ),
    ]
