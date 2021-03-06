# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-11-12 14:53
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.sites.models import Site
from clublink.clubs.models import Club

def move_clubs(apps, schema_editor):
    # For all pages already in the database, we want to assume that it is meant for the Canadian site
    site, created = Site.objects.get_or_create(domain='localhost:8000', name='Canada')
    Club.objects.update(site=site)

class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0072_auto_20171112_1052'),
    ]

    operations = [
        migrations.RunPython(move_clubs),
    ]
