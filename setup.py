#!/usr/bin/env python
from setuptools import setup

setup(
    name='RedBridge Apps Admin',
    version='1.1.1',
    long_description=__doc__,
    packages=['rb_apps_admin'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask',
        'flask-restful',
        'Flask-PyMongo',
        'python-dateutil',
        'gunicorn',
        'eventlet'
    ]
)
