# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170504_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='first_name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='player',
            name='last_name',
            field=models.CharField(max_length=25),
        ),
    ]
