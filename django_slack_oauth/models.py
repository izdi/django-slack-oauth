# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models

from jsonfield import JSONField


class SlackOAuthRequest(models.Model):
    associated_user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)
    access_token = models.CharField(max_length=128, null=True, blank=True)
    extras = JSONField(null=True, blank=True)

    ip = models.GenericIPAddressField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Slack OAuth Request"
        verbose_name_plural = "Slack OAuth Requests"
