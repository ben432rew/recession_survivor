# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20141215_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_owned',
            name='date_bought',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
