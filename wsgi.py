import sys
import os.path
import json
from werkzeug.wsgi import get_path_info
from werkzeug.exceptions import NotFound

# Extend the path to find our imported modules
sys.path.insert(0, os.path.dirname(__file__))
from run import create_app

class PathDispatcher(object):
	"""Middleware routing from the URLs to individual applications
	respective to the parliament.
	"""
	def __init__(self):
		"""Create application instances for all parliaments."""
		self.instances = {}
		with open(os.path.join(os.path.dirname(__file__), 'parliaments.json'), 'r') as f:
			parliaments = json.load(f)
		for parl, conf in parliaments.items():
			self.instances[parl] = create_app(parl, conf)

	def __call__(self, environ, start_response):
		"""Return application instance respective to the parliament in
		the URL."""
		app = NotFound()
		segments = get_path_info(environ).lstrip('/').split('/', 2)
		if len(segments) >= 2:
			parl = segments[0] + '/' + segments[1]
			if parl in self.instances:
				app = self.instances[parl]
		return app(environ, start_response)

application = PathDispatcher()
