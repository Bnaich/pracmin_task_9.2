#!/usr/bin/env python3
import json
import requests
import pytest
import logging.config
logging.config.fileConfig('logging.cfg')

def compute(queries, header = 'Content-Type', header_value = 'application/json'):
    for method, key, value, response in queries:
        addr = 'http://localhost:2000/storage_server?key=' + key
        if method == 'PUT':
            answer = requests.put(addr, json=value)
        elif method == 'GET':
            answer = requests.get(addr)
        elif method == 'DELETE':
            answer = requests.delete(addr)

        full_request = '{m}'.format(m=method)
        full_request += ' '
        full_request += '{a}'.format(a=addr)
        if value:
            full_request += ' '
            full_request += '{val}'.format(val=value)

        data = answer.text
        if header_value in answer.headers[header]:
            data = json.loads(data)
        logging.info("\n-----TEST_begin----\n%s %s %s %s full_request=%s\n------TEST_end------\n",
                method, key, value, response, full_request)
        assert data == response, "request: {}".format(full_request)

def test_put_delete_simple():
    queries = [
              ['PUT', 'Max', 'Scherbakov', 'Created\n'],
              ['DELETE', 'Max', 'Scherbakov', 'OK\n']
            ]
    compute(queries)

def test_delete_before_put():
    queries = [
            ['DELETE', 'Max', '', 'Value by this Key is not exist\n'],
            ['PUT', 'Max', 'Scherbakov', 'Created\n'],
            ['DELETE', 'Max', 'Scherbakov', 'OK\n']
            ]
    compute(queries)
    
def test_dublicate_key():
    queries = [
            ['PUT', 'Max', 'Scherbakov', 'Created\n'],
            ['PUT', 'Max', 'Ivanov', 'Already Exists\n'],
            ['GET', 'Max', '', 'Scherbakov'],
            ['DELETE', 'Max', 'Scherbakov', 'OK\n']
            ]
    compute(queries)

def test_some_get():
    queries = [
        ['PUT',   '30', '239', 'Created\n'],
        ['PUT',   '30', '', 'Already Exists\n'],
        ['GET',    '30', '', '239'],
        ['DELETE', '30', '', 'OK\n'],
        ['GET',    '30', '', 'Value by this Key is not exist\n'],
        ['DELETE', '30', '', 'Value by this Key is not exist\n'],
    ]
    compute(queries)

def test_several_values():
    queries = [
        ['GET',    '1', '', 'Value by this Key is not exist\n'],
        ['GET',    '2', '', 'Value by this Key is not exist\n'],
        ['GET',    '3', '', 'Value by this Key is not exist\n'],
        ['PUT',   '1', [1], 'Created\n'],
        ['PUT',   '2', [[1],[2]], 'Created\n'],
        ['PUT',   '3', 3, 'Created\n'],
        ['GET',    '1', '', [1]],
        ['GET',    '2', '', [[1], [2]]],
        ['GET',    '3', '', 3],
        ['DELETE', '1', '', 'OK\n'],
        ['DELETE', '2', '', 'OK\n'],
        ['DELETE', '3', '', 'OK\n'],
        ['DELETE', '1', '', 'Value by this Key is not exist\n'],
        ['DELETE', '2', '', 'Value by this Key is not exist\n'],
        ['DELETE', '3', '', 'Value by this Key is not exist\n']
    ]
    compute(queries)
    
