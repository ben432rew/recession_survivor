# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('final_score', models.FloatField()),
                ('date_played', models.DateTimeField(auto_now=True)),
                ('balance', models.FloatField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('snippet', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('symbol', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=50)),
                ('volume', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stock_owned',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('symbol', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('price_bought', models.FloatField()),
                ('date_bought', models.DateField()),
                ('name', models.CharField(max_length=50)),
                ('portfolio', models.ForeignKey(to='portfolio.Portfolio')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transcation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('symbol', models.CharField(max_length=50)),
                ('number_of_shares', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('account_change', models.FloatField()),
                ('portfolio', models.ForeignKey(to='portfolio.Portfolio')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='snippet',
            name='stock',
            field=models.ForeignKey(to='portfolio.Stock'),
            preserve_default=True,
        ),
    ]
