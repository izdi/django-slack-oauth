# -*- coding: utf-8 -*-

from jsonfield import JSONField

from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


__all__ = (
    'SlackUser',
    'SlackOAuthRequest',
)


@python_2_unicode_compatible
class SlackUser(models.Model):
    slacker = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, related_name='slack_user')
    access_token = models.CharField(max_length=128, null=True)
    extras = JSONField(null=True)

    def is_slacked(self):
        return self.access_token

    def __str__(self):
        return self.slacker.__str__()

    class Meta:
        db_table = 'slack_user'


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
