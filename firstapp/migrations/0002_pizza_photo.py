# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-29 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='firstapp/photos', verbose_name='Фото'),
        ),
    ]
