# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20141215_0415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock_owned',
            name='name',
        ),
    ]
