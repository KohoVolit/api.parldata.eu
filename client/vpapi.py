import requests
import json
import base64

"""Visegrad+ parliament API client module.
Contains functions to make API requests easily.
"""

__all__ = ['parliament', 'authorize', 'deauthorize', 'get', 'post', 'put', 'patch', 'delete']

SERVER_NAME = 'api.parldata.eu'
SERVER_CERT = 'server_cert_prod.pem'
PARLIAMENT = ''
PAYLOAD_HEADERS = {
	'Content-Type': 'application/json',
}

def _endpoint(resource, method):
	"""Returns URL of the given resource and method.
	http:// is used for GET method while https:// for the others.
	http:// is used for all methods on localhost.
	"""
	if method=='GET' or SERVER_NAME.startswith('localhost:') or SERVER_NAME.startswith('127.0.0.1:'):
		protocol = 'http'
	else:
		protocol = 'https'
	if PARLIAMENT:
		url = '%s://%s/%s/%s' % (protocol, SERVER_NAME, PARLIAMENT, resource)
	else:
		url = '%s://%s/%s' % (protocol, SERVER_NAME, resource)
	return url


def _jsonify_dict_values(params):
	"""Returns `params` dictionary with all values of type dictionary
	or list serialized to JSON. This is necessary for _requests_
	library to pass parameters in the query string correctly.
	"""
	return { k: json.dumps(v)	if isinstance(v, dict) or isinstance(v, list) else v
		for k, v in params.items()
	}


def parliament(parl):
	"""Sets the parliament the following requests will be sent to."""
	global PARLIAMENT
	PARLIAMENT = parl


def authorize(username, password):
	"""Sets API username and password for the following data modifying
	requests.
	"""
	s = '%s:%s' % (username, password)
	PAYLOAD_HEADERS['Authorization'] = b'Basic ' + base64.b64encode(s.encode('ascii'))


def deauthorize():
	"""Unsets API username and password - the following data modifying
	requests will be anonymous.
	"""
	PAYLOAD_HEADERS.pop('Authorization', None)


def get(resource, **kwargs):
	"""Makes a GET (read) request to the API.
	Lookup parameters are specified as keyword arguments.
	"""
	resp = requests.get(
		_endpoint(resource, 'GET'),
		params=_jsonify_dict_values(kwargs),
		verify=SERVER_CERT
	)
	resp.raise_for_status()
	return resp.json()


def post(resource, data, **kwargs):
	"""Makes a POST (create) request to the API.
	`data` contains dictionary with data of the entity(ies) to create
	and eventual parameters may be specified as keyword arguments.
	"""
	resp = requests.post(
		_endpoint(resource, 'POST'),
		params=_jsonify_dict_values(kwargs),
		data=json.dumps(data),
		headers=PAYLOAD_HEADERS,
		verify=SERVER_CERT
	)
	resp.raise_for_status()
	return resp.json()


def put(resource, data, **kwargs):
	"""Makes a PUT (replace) request to the API.
	`data` contains dictionary with data of the replacing entity and
	eventual parameters may be specified as keyword arguments.
	"""
	resp = requests.put(
		_endpoint(resource, 'PUT'),
		params=_jsonify_dict_values(kwargs),
		data=json.dumps(data),
		headers=PAYLOAD_HEADERS,
		verify=SERVER_CERT
	)
	resp.raise_for_status()
	return resp.json()


def patch(resource, data, **kwargs):
	"""Makes a PATCH (update) request to the API.
	`data` contains dictionary with fields to update and their values,
	eventual parameters may be specified as keyword arguments.
	"""
	resp = requests.patch(
		_endpoint(resource, 'PATCH'),
		params=_jsonify_dict_values(kwargs),
		data=json.dumps(data),
		headers=PAYLOAD_HEADERS,
		verify=SERVER_CERT
	)
	resp.raise_for_status()
	return resp.json()


def delete(resource):
	"""Makes a DELETE request to the API."""
	resp = requests.delete(
		_endpoint(resource, 'DELETE'),
		headers=PAYLOAD_HEADERS,
		verify=SERVER_CERT
	)
	resp.raise_for_status()
	return resp.json()
