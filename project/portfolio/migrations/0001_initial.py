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
            name='Holding',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('symbol', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('price', models.FloatField()),
                ('shares', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('slug', models.CharField(max_length=200)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='snippet',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('snippet', models.TextField()),
                ('date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stock_history',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('symbol', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='snippet',
            name='stock',
            field=models.ForeignKey(to='portfolio.Stock_history'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='holding',
            name='portfolio',
            field=models.ForeignKey(to='portfolio.Portfolio'),
            preserve_default=True,
        ),
    ]
