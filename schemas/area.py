""" Area
	A geographic area whose geometry may change over time
	JSON schema: http://popoloproject.com/schemas/area.json#
"""

from . import link

resource = {
	'schema': {
		# '_id' is added automatically by Eve framework
		'name': {
			# A primary name
			'type': 'string',
			'nullable': True,
		},
		'identifier': {
			# An issued identifier
			'type': 'string',
			'nullable': True,
		},
		'classification': {
			# An area category, e.g. city
			'type': 'string',
			'nullable': True,
		},
		'parent_id': {
			# The ID of the area that contains this area
			'type': 'objectid',
			'nullable': True,
			'data_relation': {
				'resource': 'areas',
				'field': '_id',
			},
		},
		'geometry': {
			# A geometry
			'nullable': True,
		},
		# 'created_at' is added automatically by Eve framework
		# 'updated_at' is added automatically by Eve framework
		'sources': {
			# URLs to documents from which the area is derived
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': link.schema,
			},
			'unique_elements': True,
		},
	},
	'track_changes': ('name', 'geometry'),
	'relations': {
		'parent': {
			# The area that contains this area
			'field': 'parent_id',
			'resource': 'areas',
			'fkey': '_id'
		},
	}
}