import json
import base64
from datetime import datetime, date, time

import requests
import pytz

"""Visegrad+ parliament API client module.
Contains functions for sending API requests conveniently.
"""

__all__ = [
	'parliament', 'authorize', 'deauthorize',
	'get', 'getall', 'getfirst', 'post', 'put', 'patch', 'delete',
	'timezone', 'utc_to_local', 'local_to_utc',
]

SERVER_NAME = 'api.parldata.eu'
SERVER_CERT = 'server_cert.pem'
PARLIAMENT = ''
LOCAL_TIMEZONE = None
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
	return { k: json.dumps(v) if isinstance(v, dict) or isinstance(v, list) else v
		for k, v in params.items()
	}


def parliament(parl=None):
	"""Sets the parliament the following requests will be sent to.
	Returns previous, now overwritten value.
	Used without arguments returns current value without any change.
	"""
	global PARLIAMENT
	old = PARLIAMENT
	if parl is not None:
		PARLIAMENT = parl
	return old


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


def getall(resource, **kwargs):
	"""Generator that generates sequence of all found results without paging.
	Lookup parameters are specified as keyword arguments.

	Usage:
		items = vpapi.getall(resource, where={...})
		for i in items:
			...
	"""
	page = 1
	while True:
		resp = get(resource, page=page, **kwargs)
		for item in resp['_items']:
			yield item
		if 'next' not in resp['_links']: break
		page += 1


def getfirst(resource, **kwargs):
	"""Returns first found item or None if there is none.
	Lookup parameters are specified as keyword arguments.
	"""
	resp = get(resource, **kwargs)
	return next(resp.get('_items', [resp]), None)


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
	return {}


def timezone(name):
	"""Sets the local timezone to be used by `utc_to_local()` and
	`local_to_utc()` helper functions.
	"""
	global LOCAL_TIMEZONE
	LOCAL_TIMEZONE = pytz.timezone(name)


def utc_to_local(dt_str):
	"""Converts date-, time- or datetime-string returned by API from UTC
	time to local time. The local timezone must be previously set by
	`timezone()` function.
	"""
	if LOCAL_TIMEZONE is None:
		raise ValueError('The local timezone must be set first, use vpapi.timezone()')
	if ':' not in dt_str:
		return dt_str
	format = '%Y-%m-%dT%H:%M:%S' if '-' in dt_str else '%H:%M:%S'
	dt = datetime.strptime(dt_str, format)
	dt = pytz.utc.localize(dt)
	dt = dt.astimezone(LOCAL_TIMEZONE)
	return dt.strftime(format)


def local_to_utc(dt_str):
	"""Converts date-, time- or datetime-string in ISO 8601 format from
	local time to UTC time required by API. The local timezone must be
	previously set by `timezone()` function.
	"""
	if LOCAL_TIMEZONE is None:
		raise ValueError('The local timezone must be set first, use vpapi.timezone()')
	if ':' not in dt_str:
		return dt_str
	format = '%Y-%m-%dT%H:%M:%S' if '-' in dt_str else '%H:%M:%S'
	dt = dt_str.strptime(dt_str, format)
	dt = LOCAL_TIMEZONE.localize(dt)
	dt = dt.astimezone(pytz.utc)
	return dt.strftime(format)
