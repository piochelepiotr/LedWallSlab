# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_auto_20160715_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='creation',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 15, 15, 49, 56, 489680, tzinfo=utc), verbose_name='Creation', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configuration',
            name='modification',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 7, 15, 15, 50, 19, 753998, tzinfo=utc), verbose_name='Modification', auto_now_add=True),
            preserve_default=False,
        ),
    ]
