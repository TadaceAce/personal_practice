# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20170504_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='record',
        ),
        migrations.AddField(
            model_name='team',
            name='losses',
            field=models.IntegerField(blank=True, default='0'),
        ),
        migrations.AddField(
            model_name='team',
            name='ties',
            field=models.IntegerField(blank=True, default='0'),
        ),
        migrations.AddField(
            model_name='team',
            name='wins',
            field=models.IntegerField(blank=True, default='0'),
        ),
    ]
