# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 21:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core_database', '0004_auto_20170708_0148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_meetdate', models.DateField(blank=True, null=True)),
                ('meetingrequest_sent', models.DateTimeField(blank=True, null=True)),
                ('meeting_started', models.DateTimeField(blank=True, null=True)),
                ('meeting_completed', models.DateTimeField(blank=True, null=True)),
                ('report_started', models.DateTimeField(blank=True, null=True)),
                ('report_completed', models.DateTimeField(blank=True, null=True)),
                ('is_current_meeting', models.BooleanField(default=False)),
                ('entity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core_database.Entity')),
            ],
        ),
        migrations.CreateModel(
            name='MeetingCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Meetingsubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_headline', models.CharField(blank=True, max_length=300)),
                ('original_description', models.TextField(blank=True)),
                ('original_listposition', models.IntegerField(blank=True, null=True)),
                ('final_headline', models.CharField(blank=True, max_length=300)),
                ('final_description', models.TextField(blank=True)),
                ('final_listposition', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_meetingrequest', models.BooleanField(default=False)),
                ('is_invited', models.BooleanField(default=False)),
                ('accepted_invite', models.DateTimeField(blank=True, null=True)),
                ('is_attending', models.BooleanField(default=False)),
                ('is_leading', models.BooleanField(default=False)),
                ('is_reporting', models.BooleanField(default=False)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_database.Person')),
            ],
        ),
        migrations.AddField(
            model_name='meeting',
            name='meeting_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meeting_manager.MeetingCategory'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='meeting_subjects',
            field=models.ManyToManyField(to='meeting_manager.Meetingsubject'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='participants',
            field=models.ManyToManyField(to='meeting_manager.Participant'),
        ),
    ]
