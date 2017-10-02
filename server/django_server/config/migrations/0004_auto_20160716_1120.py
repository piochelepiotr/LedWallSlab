# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0003_auto_20160715_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='modification',
            field=models.DateTimeField(verbose_name='Modification', auto_now=True),
            preserve_default=True,
        ),
    ]
