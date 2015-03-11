""" Event
	An event (e.g. session, sitting, election, etc.)
	JSON schema: not part of Popolo yet
"""

from . import link

resource = {
	'schema': {
		'id': {
			# The event's unique identifier
			'type': 'string',
			'empty': False,
			'unique': True,
		},
		'name': {
			# A name given to the event
			'type': 'string',
			'nullable': True,
		},
		'identifier': {
			# An issued identifier
			'type': 'string',
			'nullable': True,
		},
		'organization_id': {
			# The ID of the organization where the event is held
			'type': 'string',
			'nullable': True,
			'data_relation': {
				'resource': 'organizations',
				'field': 'id',
			},
		},
		'type': {
			# The type of the event
			'type': 'string',
			'nullable': True,
			'allowed': ['session', 'sitting', 'sitting part', 'other'],
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
		'parent_id': {
			# The ID of the event that contains this event
			'type': 'string',
			'nullable': True,
			'data_relation': {
				'resource': 'events',
				'field': 'id',
			},
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
			# The organization where the event is held
			'field': 'organization_id',
			'resource': 'organizations',
			'fkey': 'id'
		},
		'parent': {
			# The event that contains this event
			'field': 'parent_id',
			'resource': 'events',
			'fkey': 'id'
		},
		'motions': {
			# Motions proposed at this event
			'field': 'id',
			'resource': 'motions',
			'fkey': 'legislative_session_id'
		},
		'vote_events': {
			# Vote events that occurs at this event
			'field': 'id',
			'resource': 'vote_events',
			'fkey': 'legislative_session_id'
		},
		'speeches': {
			# Speeches spoken at this event
			'field': 'id',
			'resource': 'speeches',
			'fkey': 'event_id'
		},
		'children': {
			# The sub-events of the event
			'field': 'id',
			'resource': 'events',
			'fkey': 'parent_id'
		},
	}
}
