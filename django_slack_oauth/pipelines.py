# -*- coding: utf-8 -*-

from copy import deepcopy

from .models import SlackOAuthRequest, SlackUser


__all__ = (
    'log_request',
    'slack_user',

    'debug',
)


def log_request(request, api_data):
    SlackOAuthRequest.objects.create(
        access_token=api_data.pop('access_token'),
        extras=api_data
    )

    return request, api_data


def slack_user(request, api_data):
    """
    Pipeline for backward compatibility prior to 1.0.0 version.
    In case if you're willing maintain `slack_user` table.

    """
    if request.user.is_anonymous:
        return request, api_data

    data = deepcopy(api_data)

    slacker, _ = SlackUser.objects.get_or_create(slacker=request.user)
    slacker.access_token = data.pop('access_token')
    slacker.extras = data
    slacker.save()

    return request, api_data


def debug(request, api_data):
    print("request: {}, api_data: {}".format(request, api_data))
    return request, api_data
