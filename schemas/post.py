""" Post
	A position that exists independent of the person holding it
	JSON schema: http://popoloproject.com/schemas/post.json#
"""

from . import link
from . import contact_detail

resource = {
	'schema': {
		'id': {
			# The post's unique identifier
			'type': 'string',
			'empty': False,
			'unique': True,
		},
		'label': {
			# A label describing the post
			'type': 'string',
			'nullable': True
		},
		'other_labels': {
			# An alternate label
			'type': 'list',
			'schema': {
				'type': 'string',
			},
			'unique_elements': True,
		},
		'role': {
			# The function that the holder of the post fulfills
			'type': 'string',
			'nullable': True,
		},
		'organization_id': {
			# The ID of the organization in which the post is held
			'type': 'string',
			'nullable': True,
			'data_relation': {
				'resource': 'organizations',
				'field': 'id',
			},
		},
		'area_id': {
			# The ID of the geographic area to which this post is related
			'type': 'string',
			'nullable': True,
			'data_relation': {
				'resource': 'areas',
				'field': 'id',
			},
		},
		'start_date': {
			# The date on which the post was created
			'type': 'string',
			'format': 'partialdate',
			'nullable': True,
		},
		'end_date': {
			# The date on which the post was eliminated
			'type': 'string',
			'format': 'partialdate',
			'nullable': True,
		},
		'contact_details': {
			# Means of contacting the holder of the post
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': contact_detail.schema,
			},
			'unique_elements': True,
		},
		'links': {
			# URLs to documents about the post
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
			# URLs to documents from which the post is derived
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': link.schema,
			},
			'unique_elements': True,
		},
	},
	'track_changes': ('label', 'role', 'contact_details'),
	'relations': {
		'organization': {
			# The ID of the organization in which the post is held
			'field': 'organization_id',
			'resource': 'organizations',
			'fkey': 'id'
		},
		'area': {
			# The geographic area to which this post is related
			'field': 'area_id',
			'resource': 'areas',
			'fkey': 'id'
		},
		'memberships': {
			# The memberships through which people hold the post in the organization
			'field': 'id',
			'resource': 'memberships',
			'fkey': 'post_id'
		},
	}
}
