======================================
Django Slack OAuth
======================================

Django module for handling Slack OAuth.
In order to use Slack OAuth in your project you need to create application https://api.slack.com/applications
Users must be authenticated on your site.


Install
============

``pip install django-slack-oauth``

Set up
============

1. Add ``django_slack_oauth`` to your INSTALLED_APPS settings:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_slack_oauth',
    )

2. Run ``./manage migrate``; ``South`` or ``Django>=1.7`` is required.

3. Include the application URLconf in your project urls.py:

``url(r'^slack/', include('django_slack_oauth.urls')),``

4.1 Set up in your settings, these are required:

.. code-block:: python

    SLACK_CLIENT_ID = os.environ.get('SLACK_CLIENT_ID')
    SLACK_CLIENT_SECRET = os.environ.get('SLACK_CLIENT_SECRET')
    
    # Optional parameters
    # Defaults
    SLACK_SCOPE = 'identify,read,post'
    SLACK_SUCCESS_REDIRECT_URL = '/'
    
    # These are in case slack team decides
    # to change it's endpoints
    SLACK_AUTHORIZATION_URL = 'https://slack.com/oauth/authorize'
    SLACK_OAUTH_ACCESS_URL = 'https://slack.com/api/oauth.access'

With optional settings you could provide custom scope or redirect url upon completion

4.2 To avoid forgery attacks we pass ``state`` param in authorization request on slack endpoint. This state is stored in cache. For production environments I'd highly recommend to set up your cache backend using Redis or memcached other than ``LocMemCache``. Example:

.. code-block:: python 

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
        }
    }

5. Use the url to authenticate your users in your templates

``<a href='{% url 'slack_auth' %}'>Get slacked</a>``

6. Find your token in ``slack_user`` table
