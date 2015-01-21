#!/usr/bin/env python
# Copyright 2015 Magnus Bengtsson

# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy
# of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
import os
from flask import Flask
from flask.ext import restful
from flask.ext.pymongo import PyMongo
from flask import make_response
from bson.json_util import dumps

app = Flask(__name__)
# config
#
# connect to preprod mongo using a tunnel: ssh x.x.x.x -L27017:127.0.0.1:27017
# export path to settings file: export RB_APPS_ADMIN_SETTINGS=./settings.cfg
app.config.from_envvar('RB_APPS_ADMIN_SETTINGS')
mongo = PyMongo(app)

def output_json(obj, code, headers=None):
    resp = make_response(dumps(obj), code)
    resp.headers.extend(headers or {})
    return resp

DEFAULT_REPRESENTATIONS = {'application/json': output_json}

api = restful.Api(app)
api.representations = DEFAULT_REPRESENTATIONS

import resources
