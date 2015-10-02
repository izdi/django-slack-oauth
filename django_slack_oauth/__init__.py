# -*- coding: utf-8 -*-

from django.conf import settings

default_settings = {
    'SLACK_CLIENT_ID': '11808735232.11804855140',
    'SLACK_CLIENT_SECRET': 'ca10115c8567092a2c915c24924e7663',

    'SLACK_AUTHORIZATION_URL': 'https://slack.com/oauth/authorize',
    'SLACK_OAUTH_ACCESS_URL': 'https://slack.com/api/oauth.access',
    'SLACK_SUCCESS_REDIRECT_URL': '/',

    'SLACK_SCOPE': 'identify,read,post',
}


class Settings(object):
    def __init__(self, app_settings, defaults):
        for k, v in defaults.iteritems():
            setattr(self, k, getattr(app_settings, k, v))

settings = Settings(settings, default_settings)