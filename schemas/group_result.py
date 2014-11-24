""" Group result
	A result of a vote event within a group of voters
	JSON schema: http://www.popoloproject.com/schemas/group_result.json#
"""

schema = {
	'group_id': {
		# The ID of a group of voters
		'type': 'string',
		'nullable': True,
	},
	'group': {
		# A group of voters
		'nullable': True,
	},
	'result': {
		# The result of the vote event within a group of voters
		'type': 'string',
		'required': True,
		'empty': False,
	},	
}
