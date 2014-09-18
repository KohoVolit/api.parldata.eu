""" Log
	Information about running and past jobs (scrapers) that update the data
	Not part of Popolo standard
"""

resource = {
	'schema': {
		'id': {
			# The log's unique identifier
			'type': 'string',
			'empty': False,
			'unique': True,
		},
		'label': {
			# A label describing what parts of data the job updates
			'type': 'string',
			'nullable': True,
		},
		'status': {
			# Current state of the job execution
			'type': 'string',
			'allowed': ['running', 'finished', 'failed'],
			'required': True,
		},
		'params': {
			# Parameters the job is executed with
		},
		'file': {
			# Path and name of the file where details from the job execution are logged
			'type': 'string',
			'nullable': True,
		},
		# 'created_at' is added automatically by Eve framework
		# 'updated_at' is added automatically by Eve framework
	}
}
