"""	Motion
	A formal step to introduce a matter for consideration by an organization
	JSON schema: http://popoloproject.com/schemas/motion.json#
"""

from . import link
from . import vote_event

resource = {
	'schema': {
		# '_id' is added automatically by Eve framework
		'organization_id': {
			# The ID of the organization in which the motion is proposed
			'type': 'objectid',
			'nullable': True,
			'data_relation': {
				'resource': 'organizations',
				'field': '_id',
			},
		},
		'context_id': {
			# The ID of the legislative context in which the motion is proposed
			'type': 'string',
			'nullable': True,
		},
		'context': {
			# The legislative context in which the motion is proposed
			'nullable': True,
		},
		'creator_id': {
			# The ID of the person who proposed the motion
			'type': 'objectid',
			'nullable': True,
			'data_relation': {
				'resource': 'people',
				'field': '_id',
			},
		},
		'text': {
			# The transcript or text of the motion
			'type': 'string',
			'nullable': True,
		},
		'classification': {
			# A motion category, e.g. adjournment
			'type': 'string',
			'nullable': True,
		},
		'object': {
			# A resource that the motion specifically references
			'nullable': True,
		},
		'date': {
			# The date on which the motion was proposed
			'type': 'datetime',
			'nullable': True,
		},
		'requirement': {
			# The requirement for the motion to be adopted
			'type': 'string',
			'nullable': True,
		},
		'result': {
			# The result of the motion
			'type': 'string',
			'nullable': True,
			'allowed': ['pass', 'fail']
		},
		'vote_events': {
			# Events at which people vote on the motion
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': vote_event.resource['schema'],
			},
			'unique_elements': True,
		},
		# 'created_at' is added automatically by Eve framework
		# 'updated_at' is added automatically by Eve framework
		'sources': {
			# URLs to documents from which the motion is derived
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
			# The organization in which the motion is proposed
			'field': 'organization_id',
			'resource': 'organizations',
			'fkey': '_id'
		},
		'creator': {
			# The person who proposed the motion
			'field': 'creator_id',
			'resource': 'people',
			'fkey': '_id'
		},
	}
}
