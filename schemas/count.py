""" Count
	The number of votes for an option in a vote event
	JSON schema: http://popoloproject.com/schemas/count.json#
"""

resource = {
	'schema': {
		# '_id' is added automatically by Eve framework
		'vote_event_id': {
			# The ID of a vote event
			'type': 'objectid',
			'required': True,
			'empty': False,
			'data_relation': {
				'resource': 'vote_events',
				'field': '_id',
			},
		},
		'option': {
			# An option in a vote event
			'type': 'string',
			'required': True,
			'empty': False,
			'allowed': ['yes', 'no', 'abstain', 'absent', 'not voting', 'paired']
		},
		'value': {
			# The number of votes for an option
			'type': 'integer',
			'required': True,
			'empty': False,
		},
	},
	'relations': {
		'vote_event': {
			# A vote event
			'field': 'vote_event_id',
			'resource': 'vote_events',
			'fkey': '_id'
		},
	}
}
