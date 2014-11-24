""" Event
	An event (eg. session, sitting, election, etc.)
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
				'resource': 'organization',
				'field': 'id',
			},
		},
		'type': {
			# The type of the event
			'type': 'string',
			'nullable': True,
			'allowed': ['session', 'sitting', 'other'],
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
			'resource': 'organization',
			'fkey': 'id'
		},
		'parent': {
			# The event that contains this event
			'field': 'parent_id',
			'resource': 'events',
			'fkey': 'id'
		},
		'speeches': {
			# Speeches spoken at this event
			'field': 'id',
			'resource': 'speeches',
			'fkey': 'event_id'
		},
	}
}
