# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-08 22:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('open_races', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='race',
            old_name='news_website',
            new_name='races_website',
        ),
    ]
