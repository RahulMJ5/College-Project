# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-01 17:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financialcompaniesapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companysales',
            name='SixMonthsRevenue',
        ),
    ]
