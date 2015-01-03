# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20150103_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whole_game',
            name='portfolio',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
