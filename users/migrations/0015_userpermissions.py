# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-04 02:14
# flake8: noqa
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20170418_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_access_cms', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='permissions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]