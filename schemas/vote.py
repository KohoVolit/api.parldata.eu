""" Vote
	A voter's vote in a vote event
	JSON schema: http://popoloproject.com/schemas/vote.json#
"""

resource = {
	'schema': {
		# '_id' is added automatically by Eve framework
		'vote_event_id': {
			# The ID of a vote event
			'type': 'objectid',
			'required': True,
			'empty': False,
			'data_relation': {
				'resource': 'vote_events',
				'field': '_id',
			},
		},
		'voter_id': {
			# The ID of the person or organization that is voting
			'type': 'objectid',
			'nullable': True,
			'data_relation': {
				'resource': 'people',
				'field': '_id',
			},
		},
		'option': {
			# The option chosen by the voter, whether actively or passively
			'type': 'string',
			'required': True,
			'empty': False,
			'allowed': ['yes', 'no', 'abstain', 'absent', 'not voting', 'paired']
		},
		'group_id': {
			#The ID of the voter's primary political group
			'type': 'objectid',
			'nullable': True,
			'data_relation': {
				'resource': 'organizations',
				'field': '_id',
			},
		},
		'role': {
			# The voter's role in the event
			'type': 'string',
			'nullable': True,
		},
		'weight': {
			# The weight of the voter's vote
			'type': 'integer',
			'nullable': True,
			'default': 1,
		},
		'pair_id': {
			# The ID of the person with whom the voter is paired
			'type': 'objectid',
			'nullable': True,
			'data_relation': {
				'resource': 'people',
				'field': '_id',
			},
		},
	},
	'relations': {
		'vote_event': {
			# A vote event
			'field': 'vote_event_id',
			'resource': 'vote_events',
			'fkey': '_id'
		},
		'voter': {
			# The person or organization that is voting
			'field': 'voter_id',
			'resource': 'people',
			'fkey': '_id'
		},
		'group': {
			# The voter's primary political group
			'field': 'group_id',
			'resource': 'organizations',
			'fkey': '_id'
		},
		'pair': {
			# The person with whom the voter is paired
			'field': 'pair_id',
			'resource': 'people',
			'fkey': '_id'
		},
	}
}
