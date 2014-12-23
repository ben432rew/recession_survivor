# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20141215_0533'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Transcation',
            new_name='Transaction',
        ),
    ]
