# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-05-21 21:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit_Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('text', models.CharField(max_length=300)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
