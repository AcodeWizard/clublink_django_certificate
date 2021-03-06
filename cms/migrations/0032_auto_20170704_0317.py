# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-04 07:17
from __future__ import unicode_literals

from django.db import migrations


CREATE = {}

RENAME = {
    'events/weddings': {
        'copy_2': 'guarantee',
        'copy_3': 'contact',
    },
}

IMAGES_RENAME = {}


def migrate(apps, schema_editor):
    Club = apps.get_model('clubs', 'Club')
    ClubImage = apps.get_model('cms', 'ClubImage')
    ClubPage = apps.get_model('cms', 'ClubPage')
    ClubSnippet = apps.get_model('cms', 'ClubSnippet')

    for club in Club.objects.all():
        for page_path in IMAGES_RENAME:
            try:
                page = ClubPage.objects.get(club=club, full_path=page_path)
            except ClubPage.DoesNotExist:
                pass
            else:
                for slug in IMAGES_RENAME[page_path]:
                    old_slug = IMAGES_RENAME[page_path][slug]
                    ClubImage.objects.filter(page=page, slug=slug).delete()
                    images = ClubImage.objects.filter(page=page, slug=old_slug)
                    images.update(slug=slug)

        for page_path in RENAME:
            try:
                page = ClubPage.objects.get(club=club, full_path=page_path)
            except ClubPage.DoesNotExist:
                pass
            else:
                for slug in RENAME[page_path]:
                    old_slug = RENAME[page_path][slug]
                    ClubSnippet.objects.filter(page=page, slug=slug).delete()
                    snippets = ClubSnippet.objects.filter(page=page, slug=old_slug)
                    snippets.update(slug=slug)

        for page_path in CREATE:
            try:
                page = ClubPage.objects.get(club=club, full_path=page_path)
            except ClubPage.DoesNotExist:
                pass
            else:
                for slug in CREATE[page_path]:
                    content = CREATE[page_path][slug]
                    snippet, _ = ClubSnippet.objects.update_or_create(
                        page=page, locale='en', slug=slug, defaults={'content': content})


def reverse_migrate(apps, schema_editor):
    Club = apps.get_model('clubs', 'Club')
    ClubImage = apps.get_model('cms', 'ClubImage')
    ClubPage = apps.get_model('cms', 'ClubPage')
    ClubSnippet = apps.get_model('cms', 'ClubSnippet')

    for club in Club.objects.all():
        for page_path in IMAGES_RENAME:
            try:
                page = ClubPage.objects.get(club=club, full_path=page_path)
            except ClubPage.DoesNotExist:
                pass
            else:
                for slug in IMAGES_RENAME[page_path]:
                    old_slug = IMAGES_RENAME[page_path][slug]
                    ClubImage.objects.filter(page=page, slug=old_slug).delete()
                    images = ClubImage.objects.filter(page=page, slug=slug)
                    images.update(slug=old_slug)

        for page_path in RENAME:
            try:
                page = ClubPage.objects.get(club=club, full_path=page_path)
            except ClubPage.DoesNotExist:
                pass
            else:
                for slug in RENAME[page_path]:
                    old_slug = RENAME[page_path][slug]
                    ClubSnippet.objects.filter(page=page, slug=old_slug).delete()
                    snippets = ClubSnippet.objects.filter(page=page, slug=slug)
                    snippets.update(slug=old_slug)


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0031_auto_20170702_1749'),
    ]

    operations = [
        migrations.RunPython(migrate, reverse_migrate),
    ]
