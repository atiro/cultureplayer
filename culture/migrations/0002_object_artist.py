# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('culture', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='object',
            name='artist',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
    ]
