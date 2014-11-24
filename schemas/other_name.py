""" Other name
	An alternate or former name
	JSON schema: http://www.popoloproject.com/schemas/other_name.json#
"""

schema = {
	'name': {
		# An alternate or former name
		'type': 'string',
		'required': True,
		'empty': False,
	},
	'family_name': {
		# One or more family names
		'type': 'string',
		'nullable': True,
	},
	'given_name': {
		# One or more primary given names
		'type': 'string',
		'nullable': True,
	},
	'additional_name': {
		# One or more secondary given names
		'type': 'string',
		'nullable': True,
	},
	'honorific_prefix': {
		# One or more honorifics preceding a person's name
		'type': 'string',
		'nullable': True,
	},
	'honorific_suffix': {
		# One or more honorifics following a person's name
		'type': 'string',
		'nullable': True,
	},
	'patronymic_name': {
		# One or more patronymic names
		'type': 'string',
		'nullable': True,
	},
	'start_date': {
		# The date on which the name was adopted
		'type': 'string',
		'format': 'partialdate',
		'nullable': True,
	},
	'end_date': {
		# The date on which the name was abandoned
		'type': 'string',
		'format': 'partialdate',
		'nullable': True,
	},
	'note': {
		# A note, e.g. 'Birth name'
		'type': 'string',
		'nullable': True,
	},
}


