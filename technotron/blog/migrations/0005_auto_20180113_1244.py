# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-13 07:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180113_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 13, 7, 14, 46, 256910, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 13, 7, 14, 46, 254910, tzinfo=utc)),
        ),
    ]
