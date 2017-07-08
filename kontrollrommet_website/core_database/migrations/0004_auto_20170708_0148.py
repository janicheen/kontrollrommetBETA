# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-07 23:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core_database', '0003_auto_20170708_0054'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntityToPropertyRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_database.Entity')),
                ('propertyitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_database.Property')),
            ],
        ),
        migrations.CreateModel(
            name='EntityToPropertyRelationCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PersonfunctionCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PersonToEntityRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_database.Entity')),
                ('function', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_database.PersonfunctionCategory')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_database.Person')),
            ],
        ),
        migrations.AddField(
            model_name='entitytopropertyrelation',
            name='relation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_database.EntityToPropertyRelationCategory'),
        ),
    ]
