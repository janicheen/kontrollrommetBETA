# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 12:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meeting_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='meetingsubject',
            unique_together=set([('meeting', 'listposition_on_report'), ('meeting', 'subject'), ('meeting', 'listposition_on_request')]),
        ),
    ]