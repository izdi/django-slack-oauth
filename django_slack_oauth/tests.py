from django.test import TestCase
from django.conf import settings


class TestModuleSetup(TestCase):
    slack_settings = [
        'SLACK_CLIENT_ID',
        'SLACK_CLIENT_SECRET',
        'SLACK_AUTHORIZATION_URL',
        'SLACK_OAUTH_ACCESS'
    ]

    def test_settings(self):
        for setting_var in self.slack_settings:
            if not hasattr(settings, setting_var):
                raise self.fail('Set up %s in your project settings' % setting_var)