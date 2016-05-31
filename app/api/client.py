# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from flask import Blueprint, request

from app.lib.response import json_response

client = Blueprint('', __name__)


@client.route('/')
def test():
    return json_response('Hello, World!')
