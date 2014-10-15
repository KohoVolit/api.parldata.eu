"""	Speech
	???
	JSON schema: ???
"""

from . import link

resource = {
	'schema': {
		'id': {
			# The speech's unique identifier
			'type': 'string',
			'empty': False,
			'unique': True,
		},
		'organization_id': {
			# The ID of the organization in which the speech takes place
			'type': 'string',
			'nullable': True,
			'data_relation': {
				'resource': 'organizations',
				'field': 'id',
			},
		},
		'legislative_session_id': {
			# The ID of the legislative session in which the speech takes place
			'type': 'string',
			'nullable': True,
		},
		'legislative_session': {
			# The legislative session in which the speech takes place
			'nullable': True,
		},
		'section': {
			# The debate section in which the speech takes place
			'nullable': True,
		},
		'speaker_id': {
			# The ID of the person who gave the speech
			'type': 'string',
			'nullable': True,
			'data_relation': {
				'resource': 'people',
				'field': 'id',
			},
		},
		'label': {
			# A label descibing the speaker's function or affiliation
			'type': 'string',
			'nullable': True,
		},
		'start_date': {
			# The time at which the speech begins
			'type': 'datetime',
			'nullable': True,
		},
		'end_date': {
			# The time at which the speech ends
			'type': 'datetime',
			'nullable': True,
		},
		'number': {
			# The number of the speech within a debate
			'type': 'integer',
			'nullable': True,
		},
		'type': {
			# A type of speech, e.g. question
			'type': 'string',
			'nullable': True,
			'allowed': ['speech', 'question', 'answer', 'narrative', 'scene', 'summary', 'other']
		},
		'text': {
			# The transcript or text of the speech
			'type': 'string',
			'nullable': True,
		},
		# 'created_at' is added automatically by Eve framework
		# 'updated_at' is added automatically by Eve framework
		'sources': {
			# URLs to documents from which the speech is derived
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': link.schema,
			},
			'unique_elements': True,
		},
	},
	'relations': {
		'organization': {
			# The organization in which the speech takes place
			'field': 'organization_id',
			'resource': 'organizations',
			'fkey': 'id'
		},
		'speaker': {
			# The person who gave the speech
			'field': 'speaker_id',
			'resource': 'people',
			'fkey': 'id'
		},
	}
}
