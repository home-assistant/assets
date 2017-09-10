#!/usr/bin/python3
#
# Copyright (c) 2017, Fabian Affolter <fabian@affolter-engineering.ch>
# Released under the ASL 2.0 license. See LICENSE.md file for details.
#
import random
import time
import paho.mqtt.client as mqtt

timestamp = int(time.time())

broker = '127.0.0.1'
port = 1883
device_name = 'ambient-box'
ambients = ['temperature', 'humidity', 'pressure']

print("Messages are published on topic %s/#... -> CTRL + C to shutdown" % device_name)

while True:
    ambient = random.choice(ambients)
    topic = '{}/{}'.format(device_name, ambient)
    message = random.randrange(0, 30, 1)

    mqttclient = mqtt.Client("ha-mqtt-aambient", protocol=mqtt.MQTTv311)
    mqttclient.connect(broker, port=int(port))
    mqttclient.publish(topic, message)
    time.sleep(2)

