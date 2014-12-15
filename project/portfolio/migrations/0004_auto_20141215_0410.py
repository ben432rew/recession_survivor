# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20141215_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_owned',
            name='date_bought',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
