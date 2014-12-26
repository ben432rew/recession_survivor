# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20141211_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
