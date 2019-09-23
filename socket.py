#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 11:20:55 2019

@author: karan
"""

from flask import Flask
from flask_socketio import SocketIO, send , emit
from flask_cors import CORS

app = Flask(__name__)
app.config["INFO"] = True
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

def some_function(p):
    print("===============")
    socketio.emit('testEmit', p)


@socketio.on('connection')
def handleMessage(asd):
    print(asd)


@socketio.on('message')
def handleMessage2(asd):
    print('Message: ' +asd)
    some_function(asd)

    
        


if __name__ == '__main__':
	socketio.run(app,host="192.168.100.20",port=7444)
