# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-03 17:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies42night', '0007_auto_20170903_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies42night.User'),
        ),
    ]