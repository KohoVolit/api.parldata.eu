#!/usr/bin/env python3

"""This file represents a WSGI interaface of the API. It creates a
separate application for each parliament and incoming requests are
dispatched to the respective application by a middleware based on path
in the URL.
"""

import sys
import os.path
import json
from werkzeug.wsgi import get_path_info
from werkzeug.exceptions import NotFound

# Extend the path to find our imported modules.
sys.path.insert(0, os.path.dirname(__file__))
from run import create_app, hateoas_app

class PathDispatcher(object):
	"""Middleware routing from the URL to particular application
	corresponding to the parliament.
	"""
	def __init__(self):
		"""Creates application instances for all parliaments."""
		self.instances = {}
		with open(os.path.join(os.path.dirname(__file__), 'conf', 'parliaments.json'), 'r') as f:
			parliaments = json.load(f)
		for c, cp in parliaments.items():
			for p in cp:
				pfx = c + '/' + p['code']
				self.instances[pfx] = create_app(c, p)

	def __call__(self, environ, start_response):
		"""Returns application instance respective to the parliament in
		the URL.
		"""
		segments = get_path_info(environ).strip('/').split('/', 2)
		if len(segments) < 2:
			app = hateoas_app
		else:
			pfx = segments[0] + '/' + segments[1]
			app = self.instances.get(pfx, NotFound())
		return app(environ, start_response)

application = PathDispatcher()
