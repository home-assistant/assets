#!/usr/bin/python3
#
# Copyright (c) 2017, Fabian Affolter <fabian@affolter-engineering.ch>
# Released under the ASL 2.0 license. See LICENSE.md file for details.
#
import random
from datetime import datetime

from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse, request

app = Flask('home-assistant-rest-ambient-sensor')
app.config['SECRET_KEY'] = 'c846b95c4eb4f8f5a76e52d8fdcee815e7f1b19f799aed511a0616115bb87694'

api = Api(app)

AMBIENT_DATA = {
    'name': 'ambient-box',
    'temperature': None,
    'humidity': None,
    'pressure': None,
    'led': None,
}

class Api(Resource):
    def get(self):
        return {'description': 'home assistant demo maker faire'}

api.add_resource(Api, '/')

class Status(Resource):
    def get(self):
        AMBIENT_DATA['temperature'] = random.randrange(0, 30, 1)
        AMBIENT_DATA['humidity'] = random.randrange(40, 100, 1)
        AMBIENT_DATA['pressure'] = random.randrange(900, 1050, 1)
        return AMBIENT_DATA

api.add_resource(Status, '/api/states')

class Temperature(Resource):
    def get(self):
        return {'value': random.randrange(0, 30, 1)}

api.add_resource(Temperature, '/api/temperature')

class Humidity(Resource):
    def get(self):
        return {'value': random.randrange(0, 30, 1)}

api.add_resource(Humidity, '/api/humidity')

class Pressure(Resource):
    def get(self):
        return {'value': random.randrange(0, 30, 1)}

api.add_resource(Pressure, '/api/pressure')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
