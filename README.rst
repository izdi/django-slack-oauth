======================================
Django Slack Oauth
======================================

Django module for handling Slack OAuth.
In order to use Slack OAuth in your project you need to create application https://api.slack.com/applications


Installation
============

1. Add ``django_slack_oauth`` to your INSTALLED_APPS settings:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'djslack',
    )

2. Run ``./manage syncdb`` to add table for storing token.

3. Include the djslack URLconf in your project urls.py:

``url(r'^slack/', include('django_slack_oauth.urls')),``

4. Set up in your settings, these are required:

.. code-block:: python

    SLACK_CLIENT_ID = os.environ.get('SLACK_CLIENT_ID')
    SLACK_CLIENT_SECRET = os.environ.get('SLACK_CLIENT_SECRET')
    SLACK_AUTHORIZATION_URL = 'https://slack.com/oauth/authorize'
    SLACK_OAUTH_ACCESS = 'https://slack.com/api/oauth.access'

Also you can provide in your settings custom scope with ``SLACK_SCOPE`` attribute.
Default scope is ``identify,read,post``

5. Use the url to authenticate your users in your templates

``<a href='{% url 'slack_auth' %}'>Get slacked</a>``

6. Find your token in ``slack_user`` table
