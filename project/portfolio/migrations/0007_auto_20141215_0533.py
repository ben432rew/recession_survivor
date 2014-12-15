# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_remove_stock_owned_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='final_score',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
