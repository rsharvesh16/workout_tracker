# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2024-04-11 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0010_auto_20240411_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='image',
        ),
        migrations.AddField(
            model_name='workout',
            name='image_blob',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]
