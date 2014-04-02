# -*- coding: UTF-8 -*-

import requests
import json
import base64

SERVER_NAME = 'http://localhost:5000'
PAYLOAD_HEADERS = {
	'Content-Type': 'application/json',
}

def _endpoint(resource):
	return '%s/%s' % (SERVER_NAME, resource)

def _urlize(params):
	return { k: json.dumps(v) for k, v in params.items() }

def authorization(username, password):
	s = '%s:%s' % (username, password)
	PAYLOAD_HEADERS['Authorization'] = b'Basic ' + base64.b64encode(s.encode('ascii'))

def get(resource, **kwargs):
	resp = requests.get(_endpoint(resource), params=_urlize(kwargs))
	resp.raise_for_status()
	return resp.json()

def post(resource, data):
	resp = requests.post(_endpoint(resource), json.dumps(data), headers=PAYLOAD_HEADERS)
	resp.raise_for_status()
	return resp.json()

def put(resource, data):
	resp = requests.put(_endpoint(resource), json.dumps(data), headers=PAYLOAD_HEADERS)
	resp.raise_for_status()
	return resp.json()

def patch(resource, data):
	resp = requests.patch(_endpoint(resource), json.dumps(data), headers=PAYLOAD_HEADERS)
	resp.raise_for_status()
	return resp.json()

def delete(resource, **kwargs):
	resp = requests.delete(_endpoint(resource), params=_urlize(kwargs), headers=PAYLOAD_HEADERS)
	resp.raise_for_status()
	return resp.json()
