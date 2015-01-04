# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_auto_20150103_1915'),
    ]

    operations = [
        migrations.RenameField(
            model_name='whole_game',
            old_name='portfolio',
            new_name='portfolio_id',
        ),
    ]
