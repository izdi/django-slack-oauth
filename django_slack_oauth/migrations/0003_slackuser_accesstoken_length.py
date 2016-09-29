# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_slack_oauth', '0002_slackuser_extras'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slackuser',
            name='access_token',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
