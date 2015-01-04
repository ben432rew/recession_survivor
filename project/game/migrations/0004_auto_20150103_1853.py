# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20150102_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whole_game',
            name='end_date',
            field=models.DateField(default=None, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='whole_game',
            name='game_type',
            field=models.CharField(choices=[('weekly', 'Weekly'), ('monthly', 'Monthly'), ('yearly', 'Yearly')], max_length=30),
            preserve_default=True,
        ),
    ]
