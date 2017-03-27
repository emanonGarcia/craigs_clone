# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 03:12
from __future__ import unicode_literals

from django.db import migrations
from craigslist.models import State, City


def create_cities(apps, schema_editor):
    city_list = [("Durham", "North Carolina"), ("Raleigh", "North Carolina"), ("Chapel Hill", "North Carolina"), ("Richmond", "Virginia"), ("Alexandria", "Virginia"), ("Norfolk", "Virginia")]
    for pair in city_list:
        city = pair[0]
        state = State.objects.get(state=pair[1])

        c = City(city=city, state=state)
        c.save()


class Migration(migrations.Migration):

    dependencies = [
        ('craigslist', '0002_auto_20170327_0243'),
    ]

    operations = [
        migrations.RunPython(create_cities)
    ]
