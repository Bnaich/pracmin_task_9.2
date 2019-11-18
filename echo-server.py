#!/usr/bin/env python3

import os
import redis
from flask import Flask, request
import logging.config

HOST = '0.0.0.0'  #Standart loopback inerface address (localhost)
PORT = 65432      # Port to listen on (non-privileged ports are > 1023)

logging.config.fileConfig('logging.cfg')

def cache_put(key, value):
    cache = redis.Redis('rediska', port=6379)
    cache.ping()
    if cache.exists(key):
        return True
    else:
        cache.set(key, value)
        return False

def cache_get(key):
    logging.debug("Get for key [%s]", key)
    cache = redis.Redis('rediska', port=6379)
    cache.ping()
    if cache.exists(key):
        return cache.get(key)
    else:
        logging.error('DB no data for key: ' + request.values.get('key'))
        return None

def cache_delete(key):
    logging.debug('delete for key %s', key)
    cache = redis.Redis('rediska', port=6379)
    cache.ping()
    if cache.exists(key):
        cache.delete(key)
        return True
    else:
        return False

app = Flask(__name__)

@app.route('/storage_server', methods=['PUT','GET','DELETE'])
def storage_server():
    key = request.args.get('key')
    if key is None:
        return 'Error! \'key\' is not specified\n', 400

    if request.method == 'PUT':
        if request.headers.get('Content-Type') != 'application/json':
            return 'Wrong Content-Type, application/json is required\n', 400
        val = request.data 
        if cache_put(key, val): return 'OK', 200
        else: return 'Created', 201
    elif request.method == 'GET':
        res = cache_get(key)
        if res is None: return 'Value by this Key is not exist\n'
        else: return app.response_class(response=res, status=200, mimetype='application/json')

    elif request.method == 'DELETE':
        if cache_delete(key): 
            return 'OK', 200
        else:
            return 'Value by this Key is not exist\n', 404
    


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
