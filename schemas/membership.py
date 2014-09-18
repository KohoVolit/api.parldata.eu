""" Membership
	A relationship between a person and an organization
	JSON schema: http://popoloproject.com/schemas/membership.json#
"""

from . import link
from . import contact_detail

resource = {
	'schema': {
		'id': {
			# The membership's unique identifier
			'type': 'string',
			'empty': False,
			'unique': True,
		},
		'label': {
			# A label describing the membership
			'type': 'string',
			'nullable': True,
		},
		'role': {
			# The role that the person fulfills in the organization
			'type': 'string',
			'nullable': True,
		},
		'member': {
			# The person or organization that is a member of the organization
		},
		'person_id': {
			# The ID of the person who is a party to the relationship
			'type': 'string',
			'nullable': True,
			'data_relation': {
				'resource': 'people',
				'field': '_id',
			},
		},
		'organization_id': {
			# The ID of the organization that is a party to the relationship
			'type': 'string',
			'nullable': True,
			'data_relation': {
				'resource': 'organizations',
				'field': '_id',
			},
		},
		'post_id': {
			# The ID of the post held by the person in the organization through this membership
			'type': 'string',
			'nullable': True,
			'data_relation': {
				'resource': 'posts',
				'field': '_id',
			},
		},
		'on_behalf_of_id': {
			# The ID of the organization on whose behalf the person is a party to the relationship
			'type': 'string',
			'nullable': True,
			'data_relation': {
				'resource': 'organizations',
				'field': '_id',
			},
		},
		'area_id': {
			# The ID of the geographic area to which this membership is related
			'type': 'string',
			'nullable': True,
			'data_relation': {
				'resource': 'areas',
				'field': '_id',
			},
		},
		'start_date': {
			# The date on which the relationship began
			'type': 'string',
			'format': 'partialdate',
			'nullable': True,
		},
		'end_date': {
			# The date on which the relationship ended
			'type': 'string',
			'format': 'partialdate',
			'nullable': True,
		},
		'contact_details': {
			# Means of contacting the person who is a party to the relationship
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': contact_detail.schema,
			},
			'unique_elements': True,
		},
		'links': {
			# URLs to documents about the membership
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': link.schema,
			},
			'unique_elements': True,
		},
		# 'created_at' is added automatically by Eve framework
		# 'updated_at' is added automatically by Eve framework
		'sources': {
			# URLs to documents from which the membership is derived
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': link.schema,
			},
			'unique_elements': True,
		},
	},
	'track_changes': ('label', 'contact_details'),
	'relations': {
		'person': {
			# The person who is a party to the relationship
			'field': 'person_id',
			'resource': 'people',
			'fkey': '_id'
		},
		'organization': {
			# The organization that is a party to the relationship
			'field': 'organization_id',
			'resource': 'organizations',
			'fkey': '_id'
		},
		'post': {
			# The post held by the person in the organization through this membership
			'field': 'post_id',
			'resource': 'posts',
			'fkey': '_id'
		},
		'on_behalf_of': {
			# The organization on whose behalf the person is a party to the relationship
			'field': 'on_behalf_of_id',
			'resource': 'organizations',
			'fkey': '_id'
		},
		'area': {
			# The geographic area to which this membership is related
			'field': 'area_id',
			'resource': 'areas',
			'fkey': '_id'
		},
	}
}
