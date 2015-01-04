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
            name='start_balance',
            field=models.FloatField(default=10000),
            preserve_default=True,
        ),
    ]
