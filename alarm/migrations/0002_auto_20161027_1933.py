# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 13:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alarm', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='api',
            old_name='from_no',
            new_name='from_number',
        ),
        migrations.RenameField(
            model_name='api',
            old_name='to_no',
            new_name='to_number',
        ),
    ]
