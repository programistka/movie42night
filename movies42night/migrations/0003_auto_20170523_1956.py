# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 19:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies42night', '0002_auto_20170521_2031'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Type',
            new_name='Status',
        ),
    ]