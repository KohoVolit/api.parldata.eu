""" Identifier
	An issued identifier
	JSON schema: http://popoloproject.com/schemas/identifier.json#
"""

schema = {
	'identifier': {
		# An issued identifier, e.g. a DUNS number
		'type': 'string',
		'required': True,
		'empty': False,
	},
	'scheme': {
		# An identifier scheme, e.g. DUNS
		'type': 'string',
		'nullable': True,
	},
}
