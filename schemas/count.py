""" Count
	The number of votes for an option in a vote event
	JSON schema: http://popoloproject.com/schemas/count.json#
"""

schema = {
	'option': {
		# An option in a vote event
		'type': 'string',
		'required': True,
		'empty': False,
		'allowed': ['yes', 'no', 'abstain', 'absent', 'not voting', 'paired']
	},
	'value': {
		# The number of votes for an option
		'type': 'integer',
		'required': True,
		'empty': False,
	},
	'group_id': {
		# The ID of a group of voters
		'type': 'string',
		'nullable': True,
	},
	'group': {
		# A group of voters
		'nullable': True,
	},
}
