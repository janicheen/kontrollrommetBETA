# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-23 18:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EntityCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EntityToPropertyRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PersonToEntityRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.Entity')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.Person')),
            ],
        ),
        migrations.CreateModel(
            name='PersonToEntityRelationCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyToPersonRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.Property')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.Person')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyToPersonRelationCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='propertytopersonrelation',
            name='relation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.PropertyToPersonRelationCategory'),
        ),
        migrations.AddField(
            model_name='persontoentityrelation',
            name='relation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.PersonToEntityRelationCategory'),
        ),
        migrations.AddField(
            model_name='entitytopropertyrelation',
            name='_property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.Property'),
        ),
        migrations.AddField(
            model_name='entitytopropertyrelation',
            name='entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.Entity'),
        ),
        migrations.AddField(
            model_name='entitytopropertyrelation',
            name='relation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.EntityToPropertyRelationCategory'),
        ),
        migrations.AddField(
            model_name='entity',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.EntityCategory'),
        ),
    ]