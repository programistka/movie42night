# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies42night', '0002_movie_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='description_from_filmweb',
            field=models.TextField(max_length=10000, null=True),
        ),
    ]