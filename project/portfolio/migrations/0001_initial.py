# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('symbol', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('price_bought', models.FloatField()),
                ('date_bought', models.DateField()),
                ('game', models.ForeignKey(to='game.Whole_Game')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
