# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-24 18:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entitytopropertyrelation',
            old_name='relation',
            new_name='relation_category',
        ),
        migrations.RenameField(
            model_name='persontoentityrelation',
            old_name='relation',
            new_name='relation_category',
        ),
        migrations.RenameField(
            model_name='propertytopersonrelation',
            old_name='relation',
            new_name='relation_category',
        ),
    ]