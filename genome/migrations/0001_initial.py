# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('culture', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('datetime', models.DateTimeField()),
                ('description', models.TextField()),
                ('genome_url', models.URLField()),
                ('channel', models.ForeignKey(to='genome.Channel')),
                ('related_objects', models.ManyToManyField(to='culture.Object')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
