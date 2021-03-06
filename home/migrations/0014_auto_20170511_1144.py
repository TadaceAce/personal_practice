# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 18:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20170510_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='approved',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='league',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Season'),
        ),
    ]
