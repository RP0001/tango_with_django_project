# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-05 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_auto_20190205_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(default='null', unique=True),
        ),
    ]