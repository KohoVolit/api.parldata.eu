""" Vote
	A voter's vote in a vote event
	JSON schema: http://popoloproject.com/schemas/vote.json#
"""

resource = {
	'schema': {
		'id': {
			# The vote's unique identifier
			'type': 'string',
			'empty': False,
			'unique': True,
		},
		'vote_event_id': {
			# The ID of a vote event
			'type': 'string',
			'required': True,
			'empty': False,
			'data_relation': {
				'resource': 'vote_events',
				'field': 'id',
			},
		},
		'voter_id': {
			# The ID of the person or organization that is voting
			'type': 'string',
			'nullable': True,
			'data_relation': {
				'resource': 'people',
				'field': 'id',
			},
		},
		'option': {
			# The option chosen by the voter, whether actively or passively
			'type': 'string',
			'required': True,
			'empty': False,
			'allowed': ['yes', 'no', 'abstain', 'absent', 'not voting', 'paired', 'excused']
		},
		'group_id': {
			#The ID of the voter's primary political group
			'type': 'string',
			'nullable': True,
			'data_relation': {
				'resource': 'organizations',
				'field': 'id',
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
		},
		'pair_id': {
			# The ID of the person with whom the voter is paired
			'type': 'string',
			'nullable': True,
			'data_relation': {
				'resource': 'people',
				'field': 'id',
			},
		},
	},
	'relations': {
		'vote_event': {
			# A vote event
			'field': 'vote_event_id',
			'resource': 'vote_events',
			'fkey': 'id'
		},
		'voter': {
			# The person or organization that is voting
			'field': 'voter_id',
			'resource': 'people',
			'fkey': 'id'
		},
		'group': {
			# The voter's primary political group
			'field': 'group_id',
			'resource': 'organizations',
			'fkey': 'id'
		},
		'pair': {
			# The person with whom the voter is paired
			'field': 'pair_id',
			'resource': 'people',
			'fkey': 'id'
		},
	}
}
