# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portfolio', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('date', models.DateField()),
                ('volume', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=50)),
                ('number_of_shares', models.IntegerField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('account_change', models.FloatField()),
                ('portfolio', models.ForeignKey(to='portfolio.Portfolio')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Whole_Game',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('game_type', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('balance', models.FloatField(default=10000)),
                ('final_score', models.FloatField(default=0)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('current_date', models.DateField()),
                ('current_round', models.IntegerField(default=0)),
                ('portfolio', models.ForeignKey(to='portfolio.Portfolio')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
