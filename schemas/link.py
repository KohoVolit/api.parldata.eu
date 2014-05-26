""" Link
	An URL
	JSON schema: http://popoloproject.com/schemas/link.json#
"""

schema = {
	'url': {
		# A URL
		'type': 'string',
		'format': 'url',
		'required': True,
	},
	'note': {
		# A note, e.g. 'Wikipedia page'
		'type': 'string',
		'nullable': True,
	},
}
