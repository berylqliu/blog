# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import urllib

from flask.ext.script import Manager, Server
from app import app

app.config.from_pyfile('config.py')

manager = Manager(app)
manager.add_command('server', Server(host=app.config.get('HOST'), port=app.config.get('PORT')))


if __name__ == "__main__":
    manager.run()
