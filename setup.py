import os
from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()


os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-slack-oauth',
    version='0.1',
    packages=['django_slack_oauth'],
    include_package_data=True,
    license='MIT License',
    description='Handles OAuth and stores slack token',
    long_description=README,
    author='Sergey Keller',
    author_email='izdieu@gmail.com',
    install_requires=[
        'Django>=1.6.1',
        'requests',
    ],
)