# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-08 02:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rrt_audio',
            name='audio_hrl_path',
            field=models.CharField(default=2, max_length=255, verbose_name='audio_hrl_path'),
            preserve_default=False,
        ),
    ]