# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-10 13:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Transactions',
            new_name='Transaction',
        ),
    ]
