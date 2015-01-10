""" Vote event
	An event at which people's votes are recorded
	JSON schema: http://www.popoloproject.com/schemas/vote_event.json#
"""

from . import link
from . import vote
from . import count
from . import group_result

resource = {
	'schema': {
		'id': {
			# The vote event's unique identifier
			'type': 'string',
			'empty': False,
			'unique': True,
		},
		'organization_id': {
			# The ID of the organization whose members are voting
			'type': 'string',
			'nullable': True,
			'data_relation': {
				'resource': 'organizations',
				'field': 'id',
			},
		},
		'legislative_session_id': {
			# The ID of the legislative session in which the vote occurs
			'type': 'string',
			'nullable': True,
			'data_relation': {
				'resource': 'events',
				'field': 'id',
			},
		},
		'identifier': {
			# An issued identifier
			'type': 'string',
			'nullable': True,
		},
		'motion_id': {
			# The ID of the motion being decided
			'type': 'string',
			'nullable': True,
			'data_relation': {
				'resource': 'motions',
				'field': 'id',
			},
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
		'group_results': {
			# The result of the vote event within groups of voters
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': group_result.schema,
			},
			'unique_elements': True,
		},
		'counts': {
			# The number of votes for options
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': count.schema,
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
		'organization': {
			# The organization whose members are voting
			'field': 'organization_id',
			'resource': 'organizations',
			'fkey': 'id'
		},
		'legislative_session': {
			# The legislative session in which the vote occurs
			'field': 'legislative_session_id',
			'resource': 'events',
			'fkey': 'id'
		},
		'motion': {
			# The motion being decided
			'field': 'motion_id',
			'resource': 'motions',
			'fkey': 'id'
		},
		'votes': {
			# Voters' votes
			'field': 'id',
			'resource': 'votes',
			'fkey': 'vote_event_id'
		},
	}
}
