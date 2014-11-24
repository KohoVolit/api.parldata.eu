""" Speech
	A speech of a speaker, a scene (e.g. applause), a narrative (e.g.
	"The House rose at 3:20pm"), or another part of a transcript (e.g.
	a list of bills).
	JSON schema: http://www.popoloproject.com/schemas/speech.json#
"""

from . import link

resource = {
	'schema': {
		'id': {
			# The speech's unique identifier
			'type': 'string',
			'empty': False,
			'unique': True,
		},
		'creator_id': {
			# The ID of the person who is speaking
			'type': 'string',
			'nullable': True,
			'data_relation': {
				'resource': 'people',
				'field': 'id',
			},
		},
		'role': {
			# The speaker's role while speaking
			'type': 'string',
			'nullable': True,
		},
		'attribution_text': {
			# The text identifying the speaker
			'type': 'string',
			'nullable': True,
		},
		'audience_id': {
			# The ID of the person to whom the speaker is speaking
			'type': 'string',
			'nullable': True,
			'data_relation': {
				'resource': 'people',
				'field': 'id',
			},
		},
		'text': {
			# The transcript or text of the speech
			'type': 'string',
			'nullable': True,
		},
		'audio': {
			# The audio recording of the speech
			'type': 'string',
			'format': 'url',
			'nullable': True,
		},
		'date': {
			# The time at which the speech is spoken
			'type': 'datetime',
			'nullable': True,
		},
		'title': {
			# A name given to the speech
			'type': 'string',
			'nullable': True,
		},
		'type': {
			# The type of the part of the transcript
			'type': 'string',
			'nullable': True,
			'allowed': ['speech', 'question', 'answer', 'scene', 'narrative',
				'summary', 'other'],
		},
		'position': {
			# The position of the speech within a transcript
			'type': 'integer',
			'nullable': True,
		},
		'event_id': {
			# The ID of the event at which the speech is spoken
			'type': 'string',
			'nullable': True,
			'data_relation': {
				'resource': 'events',
				'field': 'id',
			},
		},
		# 'created_at' is added automatically by Eve framework
		# 'updated_at' is added automatically by Eve framework
		'sources': {
			# URLs to documents from which the speech is derived
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': link.schema,
			},
			'unique_elements': True,
		},
	},
	'save_files': ('audio', ),
	'relations': {
		'creator': {
			# The person who is speaking
			'field': 'creator_id',
			'resource': 'people',
			'fkey': 'id'
		},
		'audience': {
			# The person to whom the speaker is speaking
			'field': 'audience_id',
			'resource': 'people',
			'fkey': 'id'
		},
		'event': {
			# The event at which the speech is spoken
			'field': 'event_id',
			'resource': 'events',
			'fkey': 'id'
		},
	}
}
