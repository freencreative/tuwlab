# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('isbn', models.BigIntegerField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('memo', jsonfield.fields.JSONField(default={})),
            ],
        ),
    ]
