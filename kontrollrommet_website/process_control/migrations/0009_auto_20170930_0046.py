# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-29 22:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('process_control', '0008_auto_20170924_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='case_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]