# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('django_slack_oauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slackuser',
            name='extras',
            field=jsonfield.fields.JSONField(null=True),
        ),
    ]
