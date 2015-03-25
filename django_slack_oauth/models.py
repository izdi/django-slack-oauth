from django.conf import settings
from django.db import models


class SlackUser(models.Model):
    slacker = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, related_name='slack_user')
    access_token = models.CharField(max_length=64, null=True)

    def is_slacked(self):
        return self.access_token

    def __unicode__(self):
        return self.slacker

    class Meta:
        db_table = 'slack_user'