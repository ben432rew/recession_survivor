# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='whole_game',
            name='total_rounds',
            field=models.IntegerField(default=12),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='whole_game',
            name='end_date',
            field=models.DateField(default=None),
            preserve_default=True,
        ),
    ]
