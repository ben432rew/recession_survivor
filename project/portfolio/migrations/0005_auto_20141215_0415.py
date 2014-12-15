# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20141215_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='date_played',
            field=models.DateField(auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transcation',
            name='date_created',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
