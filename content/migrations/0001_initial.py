# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('pictures', models.CharField(max_length=150)),
                ('videos', models.CharField(max_length=200)),
                ('coords', models.CharField(max_length=20)),
                ('type_activity', models.CharField(max_length=50)),
                ('city_id', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('pictures', models.CharField(max_length=150)),
                ('videos', models.CharField(max_length=200)),
                ('coords', models.CharField(max_length=30)),
                ('size', models.CharField(max_length=30)),
                ('altitude', models.CharField(max_length=30)),
                ('climate', models.CharField(max_length=20)),
                ('population', models.CharField(max_length=20)),
                ('time_zone', models.CharField(max_length=20)),
                ('languages', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('pictures', models.CharField(max_length=150)),
                ('script', models.CharField(max_length=30)),
                ('spoken_in', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
