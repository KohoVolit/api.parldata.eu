""" Organization
	A group with a common purpose or reason for existence that goes beyond the set of people belonging to it
	JSON schema: http://www.popoloproject.com/schemas/organization.json#
	Note. Organization.votes property is missing because Vote.voter is restricted to be a person in this implementation.
"""

from . import identifier
from . import link
from . import other_name
from . import contact_detail
from . import change

resource = {
	'schema': {
		'id': {
			# The organization's unique identifier
			'type': 'string',
			'empty': False,
			'unique': True,
		},
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
			'unique_elements': True,
		},
		'classification': {
			# An organization category, e.g. committee
			'type': 'string',
			'nullable': True,
		},
		'parent_id': {
			# The ID of the organization that contains this organization
			'type': 'string',
			'nullable': True,
			'data_relation': {
				'resource': 'organizations',
				'field': 'id',
			},
		},
		'area_id': {
			# The ID of the geographic area to which this organization is related
			'type': 'string',
			'nullable': True,
			'data_relation': {
				'resource': 'areas',
				'field': 'id',
			},
		},
		'abstract': {
			# A one-line description of an organization
			'type': 'string',
			'nullable': True,
		},
		'description': {
			# An extended description of an organization
			'type': 'string',
			'nullable': True,
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
	'track_changes': ('name', 'image', 'contact_details'),
	'save_files': ('image', ),
	'relations': {
		'parent': {
			# The organization that contains this organization
			'field': 'parent_id',
			'resource': 'organizations',
			'fkey': 'id'
		},
		'area': {
			# The geographic area to which this organization is related
			'field': 'area_id',
			'resource': 'areas',
			'fkey': 'id'
		},
		'memberships': {
			# The relationships to which the organization is a party
			'field': 'id',
			'resource': 'memberships',
			'fkey': 'organization_id'
		},
		'posts': {
			# Posts within the organization
			'field': 'id',
			'resource': 'posts',
			'fkey': 'organization_id'
		},
		'motions': {
			# Motions within the organization
			'field': 'id',
			'resource': 'motions',
			'fkey': 'organization_id'
		},
		'vote_events': {
			# Vote events in which members of the organization are voting
			'field': 'id',
			'resource': 'vote_events',
			'fkey': 'organization_id'
		},
		'children': {
			# The sub-organizations of the organization
			'field': 'id',
			'resource': 'organizations',
			'fkey': 'parent_id'
		},
	},
}
