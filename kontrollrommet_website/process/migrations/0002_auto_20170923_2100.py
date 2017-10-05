# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-23 19:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
        ('process', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='executive_entity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resources.Entity'),
        ),
        migrations.AddField(
            model_name='plan',
            name='executive_entity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resources.Entity'),
        ),
        migrations.AddField(
            model_name='result',
            name='executive_entity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resources.Entity'),
        ),
    ]