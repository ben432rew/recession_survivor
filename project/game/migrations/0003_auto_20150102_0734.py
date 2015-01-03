# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20150102_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whole_game',
            name='end_date',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='whole_game',
            name='start_date',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
