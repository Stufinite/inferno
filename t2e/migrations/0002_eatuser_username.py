# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-22 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t2e', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eatuser',
            name='userName',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
