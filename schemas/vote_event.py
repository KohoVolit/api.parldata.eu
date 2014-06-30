""" Vote event
	An event at which people's votes are recorded
	JSON schema: http://popoloproject.com/schemas/vote_event.json#
"""

from . import link
from . import vote
from . import count

resource = {
	'schema': {
		# '_id' is added automatically by Eve framework
		'identifier': {
			# An issued identifier
			'type': 'string',
			'nullable': True,
		},
		'motion_id': {
			# The ID of the motion being decided
			'type': 'objectid',
			'nullable': True,
			'data_relation': {
				'resource': 'motions',
				'field': '_id',
			},
		},
		'organization_id': {
			# The ID of the organization whose members are voting
			'type': 'objectid',
			'nullable': True,
			'data_relation': {
				'resource': 'organizations',
				'field': '_id',
			},
		},
		'context_id': {
			# The ID of the legislative context in which the vote occurs
			'type': 'string',
			'nullable': True,
		},
		'context': {
			# The legislative context in which the vote occurs
			'nullable': True,
		},
		'start_date': {
			# The time at which the event begins
			'type': 'datetime',
			'nullable': True,
		},
		'end_date': {
			# The time at which the event ends
			'type': 'datetime',
			'nullable': True,
		},
		'result': {
			# The result of the vote event
			'type': 'string',
			'nullable': True,
			'allowed': ['pass', 'fail']
		},
		'counts': {
			# The number of votes for options
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': count.resource['schema'],
			},
			'unique_elements': True,
		},
		'votes': {
			# Voters' votes
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': vote.resource['schema'],
			},
			'unique_elements': True,
		},
		# 'created_at' is added automatically by Eve framework
		# 'updated_at' is added automatically by Eve framework
		'sources': {
			# URLs to documents from which the vote event is derived
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': link.schema,
			},
			'unique_elements': True,
		},
	},
	'relations': {
		'motion': {
			# The motion being decided
			'field': 'motion_id',
			'resource': 'motions',
			'fkey': '_id'
		},
		'organization': {
			# The organization whose members are voting
			'field': 'organization_id',
			'resource': 'organizations',
			'fkey': '_id'
		},
	}
}