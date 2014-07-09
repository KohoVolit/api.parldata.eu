""" Log
	Information about running and past jobs (scrapers) that update the data
	Not part of Popolo standard
"""

resource = {
	'schema': {
		# '_id' is added automatically by Eve framework
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
