# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20170511_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='season',
            name='registration_open',
            field=models.NullBooleanField(default=True),
        ),
    ]
