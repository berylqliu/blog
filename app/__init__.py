# -*- coding:utf-8 -*-

from __future__ import absolute_import, unicode_literals

from flask import Flask
from app.api import client

app = Flask(__name__)

app.config.from_pyfile('../config.py')

app.register_blueprint(client.client, url_prefix='/api')
