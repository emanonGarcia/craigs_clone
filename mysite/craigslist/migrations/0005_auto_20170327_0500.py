# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 05:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('craigslist', '0004_auto_20170327_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='sub_category',
            field=models.CharField(max_length=30),
        ),
    ]