""" Organization
	A group with a common purpose or reason for existence that goes beyond the set of people belonging to it
	JSON schema: http://popoloproject.com/schemas/organization.json#
"""

from . import identifier
from . import link
from . import other_name
from . import contact_detail
from . import change

resource = {
	'schema': {
		# '_id' is added automatically by Eve framework
		'name': {
			# A primary name, e.g. a legally recognized name
			'type': 'string',
			'nullable': True,
		},
		'other_names': {
			# Alternate or former names
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': other_name.schema,
			},
			'unique_elements': True,
		},
		'identifiers': {
			# Issued identifiers
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': identifier.schema,
			},
			'disjoint': True,
			'unique_elements': True,
		},
		'classification': {
			# An organization category, e.g. committee
			'type': 'string',
			'nullable': True,
		},
		'parent_id': {
			# The ID of the organization that contains this organization
			'type': 'objectid',
			'nullable': True,
			'data_relation': {
				'resource': 'organizations',
				'field': '_id',
			},
		},
		'area_id': {
			# The ID of the geographic area to which this organization is related
			'type': 'objectid',
			'nullable': True,
			'data_relation': {
				'resource': 'areas',
				'field': '_id',
			},
		},
		'founding_date': {
			# A date of founding
			'type': 'string',
			'format': 'partialdate',
			'nullable': True,
		},
		'dissolution_date': {
			# A date of dissolution
			'type': 'string',
			'format': 'partialdate',
			'nullable': True,
		},
		'image': {
			# A URL of an image
			'type': 'string',
			'format': 'url',
			'nullable': True,
		},
		'contact_details': {
			# Means of contacting the organization
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': contact_detail.schema,
			},
			'unique_elements': True,
		},
		'links': {
			# URLs to documents about the organization
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
			# URLs to documents from which the organization is derived
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': link.schema,
			},
			'unique_elements': True,
		},
		'changes': {
			# List of property value changes
			# Managed automatically by callbacks when any of tracked properties change value
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': change.schema,
			},
		},
	},
	'track_changes': ('image', 'contact_details'),
	'save_files': ('image', ),
	'relations': {
		'parent': {
			# The organization that contains this organization
			'field': 'parent_id',
			'resource': 'organizations',
			'fkey': '_id'
		},
		'area': {
			# The geographic area to which this organization is related
			'field': 'area_id',
			'resource': 'areas',
			'fkey': '_id'
		},
		'memberships': {
			# The relationships to which the organization is a party
			'field': '_id',
			'resource': 'memberships',
			'fkey': 'organization_id'
		},
		'posts': {
			# Posts within the organization
			'field': '_id',
			'resource': 'posts',
			'fkey': 'organization_id'
		},
	},
}
