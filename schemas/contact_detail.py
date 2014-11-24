""" Contact detail
	A means of contacting an entity
	JSON schema: http://www.popoloproject.com/schemas/contact_detail.json#
"""

from . import link

schema = {
	'label': {
		# A human-readable label for the contact detail
		'type': 'string',
		'nullable': True,
	},
	'type': {
		# A type of medium, e.g. 'fax' or 'email'
		'type': 'string',
		'required': True,
		'empty': False,
		'allowed': ['person', 'address', 'email', 'url', 'tel', 'fax']
	},
	'value': {
		# A value, e.g. a phone number or email address
		'type': 'string',
		'required': True,
		'empty': False,
	},
	'note': {
		# A note, e.g. for grouping contact details by physical location
		'type': 'string',
		'nullable': True,
	},
	'valid_from': {
		# The date from which the contact detail is valid
		'type': 'string',
		'format': 'partialdate',
		'nullable': True,
	},
	'valid_until': {
		# The date from which the contact detail is no longer valid
		'type': 'string',
		'format': 'partialdate',
		'nullable': True,
	},
	'sources': {
		# URLs to documents from which the contact detail is derived
		'type': 'list',
		'schema': {
			'type': 'dict',
			'schema': link.schema,
		},
		'unique_elements': True,
	},
}
