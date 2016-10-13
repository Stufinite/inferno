# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-13 03:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('time2eat', '0011_auto_20161013_0448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='images/time2eat/menu.svg', upload_to='')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='time2eat.ResProf')),
            ],
        ),
    ]
