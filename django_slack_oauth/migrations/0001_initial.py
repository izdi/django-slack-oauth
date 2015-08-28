# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL)
    ]

    operations = [
        migrations.CreateModel(
            name='SlackUser',
            fields=[
                ('slacker', models.OneToOneField(related_name='slack_user', primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('access_token', models.CharField(max_length=64, null=True)),
            ],
            options={
                'db_table': 'slack_user',
            },
        ),
    ]
