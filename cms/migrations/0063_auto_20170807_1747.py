# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-07 21:47
from __future__ import unicode_literals

from django.db import migrations


NOBODY_VISIBILITY = 3


def create_aliases(apps, schema_editor):
    Club = apps.get_model('clubs', 'Club')
    ClubPage = apps.get_model('cms', 'ClubPage')

    for club in Club.objects.filter(daily_fee_location=False):
        for page in ClubPage.objects.filter(full_path__startswith='daily-fee-golf', club=club):
            page.visibility = NOBODY_VISIBILITY
            page.save()


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0062_auto_20170807_1747'),
    ]

    operations = [
        migrations.RunPython(create_aliases, lambda x, y: None),
    ]
