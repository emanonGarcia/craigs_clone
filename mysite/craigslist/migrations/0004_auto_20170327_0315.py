# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 03:15
from __future__ import unicode_literals

from django.db import migrations
from craigslist.models import Category, SubCategory


def load_cats(cat):
    sub_cats = cat.pop()
    cat = cat[0]
    c = Category(category=cat)
    c.save()

    for each in sub_cats:
        s = SubCategory(sub_category=each, category=Category.objects.get(category=cat))
        s.save()


def add_categories(apps, schema_editor):
    community_sub_cat = ['community', ['activities', 'artists', 'childcare', 'classes']]
    housing_sub_cat = ['housing', ['apts/housing', 'housing swap', 'housing wanted', 'rooms / shared', 'rooms wanted']]
    jobs_sub_cat = ['jobs', ['accounting+finance', 'admin / office', 'art / media / design', 'biotech / science', 'general labor', 'food / bev / hosp']]
    load_cats(community_sub_cat)
    load_cats(housing_sub_cat)
    load_cats(jobs_sub_cat)


class Migration(migrations.Migration):

    dependencies = [
        ('craigslist', '0003_auto_20170327_0312'),
    ]

    operations = [
        migrations.RunPython(add_categories),
    ]
