# Identifier
#     An issued identifier
#     JSON schema: http://popoloproject.com/schemas/identifier.json#
identifier_schema = {
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


# Link
#     An URL
#     JSON schema: http://popoloproject.com/schemas/link.json#
link_schema = {
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


# Other name
#     An alternate or former name
#     JSON schema: http://popoloproject.com/schemas/other_name.json#
other_name_schema = {
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


# Contact detail
#     A means of contacting an entity
#     JSON schema: http://popoloproject.com/schemas/contact_detail.json#
contact_detail_schema = {
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
			'schema': link_schema,
		},
		'unique_elements': True,
	},
}


# An entry in API managed list of changes of entity's property values
change_schema = {
	'property': {
		# Name of property which value has changed
		'type': 'string',
		'required': True,
	},
	'value': {
		# Former value of the property that has been changed
		'required': True,
	},
	'start_date': {
		# The date on which the former value began to be valid
		'type': 'string',
		'format': 'partialdate',
		'nullable': True,
	},
	'end_date': {
		# The date on which the former value ended to be valid
		'type': 'string',
		'format': 'partialdate',
		'nullable': True,
	},
}


# Person
#     A real person, alive or dead
#     JSON schema: http://popoloproject.com/schemas/person.json#
person = {
	'schema': {
		# '_id' is added automatically by Eve framework
		'name': {
			# A person's preferred full name
			'type': 'string',
			'nullable': True,
		},
		'other_names': {
			# Alternate or former names
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': other_name_schema,
			},
			'unique_elements': True,
		},
		'identifiers': {
			# Issued identifiers
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': identifier_schema,
			},
			'disjoint': True,
			'unique_elements': True,
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
		'sort_name': {
			# A name to use in an lexicographically ordered list
			'type': 'string',
			'nullable': True,
		},
		'email': {
			# A preferred email address
			'type': 'string',
			'format': 'email',
			'nullable': True,
		},
		'gender': {
			# A gender
			'type': 'string',
			'nullable': True,
			'allowed': ['male', 'female', 'other']
		},
		'birth_date': {
			# A date of birth
			'type': 'string',
			'format': 'partialdate',
			'nullable': True,
		},
		'death_date': {
			# A date of death
			'type': 'string',
			'format': 'partialdate',
			'nullable': True,
		},
		'image': {
			# A URL of a head shot
			'type': 'string',
			'format': 'url',
			'nullable': True,
		},
		'summary': {
			# A one-line account of a person's life
			'type': 'string',
			'nullable': True,
		},
		'national_identity': {
			# A national identity
			'type': 'string',
			'nullable': True,
		},
		'biography': {
			# An extended account of a person's life
			'type': 'string',
			'nullable': True,
		},
		'contact_details': {
			# Means of contacting the person
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': contact_detail_schema,
			},
			'unique_elements': True,
		},
		'links': {
			# URLs to documents about the person
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': link_schema,
			},
			'unique_elements': True,
		},
		# 'created_at' is added automatically by Eve framework
		# 'updated_at' is added automatically by Eve framework
		'sources': {
			# URLs to documents from which the person is derived
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': link_schema,
			},
			'unique_elements': True,
		},
		'changes': {
			# List of property value changes
			# Managed automatically by callbacks when any of tracked properties change_schema value
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': change_schema,
			},
		},
	},
	'track_changes': ('honorific_prefix', 'honorific_suffix', 'email', 'gender', 'image', 'national_identity', 'contact_details'),
	'save_files': ('image', ),
	'relations': {
		'memberships': {
			# The relationships to which the person is a party
			'field': '_id',
			'resource': 'memberships',
			'fkey': 'person_id'
		},
	},
}


# Organization
#     A group with a common purpose or reason for existence that goes beyond the set of people belonging to it
#     JSON schema: http://popoloproject.com/schemas/organization.json#
organization = {
	'schema': {
		# '_id' is added automatically by Eve framework
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
				'schema': other_name_schema,
			},
			'unique_elements': True,
		},
		'identifiers': {
			# Issued identifiers
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': identifier_schema,
			},
			'disjoint': True,
			'unique_elements': True,
		},
		'classification': {
			# An organization category, e.g. committee
			'type': 'string',
			'nullable': True,
		},
		'parent_id': {
			# The ID of the organization that contains this organization
			'type': 'objectid',
			'nullable': True,
			'data_relation': {
				'resource': 'organizations',
				'field': '_id',
			},
		},
		'area_id': {
			# The ID of the geographic area to which this organization is related
			'type': 'objectid',
			'nullable': True,
			'data_relation': {
				'resource': 'areas',
				'field': '_id',
			},
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
				'schema': contact_detail_schema,
			},
			'unique_elements': True,
		},
		'links': {
			# URLs to documents about the organization
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': link_schema,
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
				'schema': link_schema,
			},
			'unique_elements': True,
		},
		'changes': {
			# List of property value changes
			# Managed automatically by callbacks when any of tracked properties change value
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': change_schema,
			},
		},
	},
	'track_changes': ('image', 'contact_details'),
	'save_files': ('image', ),
	'relations': {
		'parent': {
			# The organization that contains this organization
			'field': 'parent_id',
			'resource': 'organizations',
			'fkey': '_id'
		},
		'area': {
			# The geographic area to which this organization is related
			'field': 'area_id',
			'resource': 'areas',
			'fkey': '_id'
		},
		'memberships': {
			# The relationships to which the organization is a party
			'field': '_id',
			'resource': 'memberships',
			'fkey': 'organization_id'
		},
		'posts': {
			# Posts within the organization
			'field': '_id',
			'resource': 'posts',
			'fkey': 'organization_id'
		},
	},
}


# Membership
#     A relationship between a person and an organization
#     JSON schema: http://popoloproject.com/schemas/membership.json#
membership = {
	'schema': {
		# '_id' is added automatically by Eve framework
		'label': {
			# A label describing the membership
			'type': 'string',
			'nullable': True,
		},
		'role': {
			# The role that the person fulfills in the organization
			'type': 'string',
			'nullable': True,
		},
		'member': {
			# The person or organization that is a member of the organization
		},
		'person_id': {
			# The ID of the person who is a party to the relationship
			'type': 'objectid',
			'nullable': True,
			'data_relation': {
				'resource': 'people',
				'field': '_id',
			},
		},
		'organization_id': {
			# The ID of the organization that is a party to the relationship
			'type': 'objectid',
			'nullable': True,
			'data_relation': {
				'resource': 'organizations',
				'field': '_id',
			},
		},
		'post_id': {
			# The ID of the post held by the person in the organization through this membership
			'type': 'objectid',
			'nullable': True,
			'data_relation': {
				'resource': 'posts',
				'field': '_id',
			},
		},
		'on_behalf_of_id': {
			# The ID of the organization on whose behalf the person is a party to the relationship
			'type': 'objectid',
			'nullable': True,
			'data_relation': {
				'resource': 'organizations',
				'field': '_id',
			},
		},
		'area_id': {
			# The ID of the geographic area to which this membership is related
			'type': 'objectid',
			'nullable': True,
			'data_relation': {
				'resource': 'areas',
				'field': '_id',
			},
		},
		'start_date': {
			# The date on which the relationship began
			'type': 'string',
			'format': 'partialdate',
			'nullable': True,
		},
		'end_date': {
			# The date on which the relationship ended
			'type': 'string',
			'format': 'partialdate',
			'nullable': True,
		},
		'contact_details': {
			# Means of contacting the person who is a party to the relationship
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': contact_detail_schema,
			},
			'unique_elements': True,
		},
		'links': {
			# URLs to documents about the membership
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': link_schema,
			},
			'unique_elements': True,
		},
		# 'created_at' is added automatically by Eve framework
		# 'updated_at' is added automatically by Eve framework
		'sources': {
			# URLs to documents from which the membership is derived
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': link_schema,
			},
			'unique_elements': True,
		},
	},
	'relations': {
		'person': {
			# The person who is a party to the relationship
			'field': 'person_id',
			'resource': 'people',
			'fkey': '_id'
		},
		'organization': {
			# The organization that is a party to the relationship
			'field': 'organization_id',
			'resource': 'organizations',
			'fkey': '_id'
		},
		'post': {
			# The post held by the person in the organization through this membership
			'field': 'post_id',
			'resource': 'posts',
			'fkey': '_id'
		},
		'on_behalf_of': {
			# The organization on whose behalf the person is a party to the relationship
			'field': 'on_behalf_of_id',
			'resource': 'organizations',
			'fkey': '_id'
		},
		'area': {
			# The geographic area to which this membership is related
			'field': 'area_id',
			'resource': 'areas',
			'fkey': '_id'
		},
	}
}


# Post
#     A position that exists independent of the person holding it
#     JSON schema: http://popoloproject.com/schemas/post.json#
post = {
	'schema': {
		# '_id' is added automatically by Eve framework
		'label': {
			# A label describing the post
			'type': 'string',
			'nullable': True
		},
		'other_labels': {
			# An alternate label
			'type': 'list',
			'schema': {
				'type': 'string',
			},
			'unique_elements': True,
		},
		'role': {
			# The function that the holder of the post fulfills
			'type': 'string',
			'nullable': True,
		},
		'organization_id': {
			# The ID of the organization in which the post is held
			'type': 'objectid',
			'nullable': True,
			'data_relation': {
				'resource': 'organizations',
				'field': '_id',
			},
		},
		'area_id': {
			# The ID of the geographic area to which this post is related
			'type': 'objectid',
			'nullable': True,
			'data_relation': {
				'resource': 'areas',
				'field': '_id',
			},
		},
		'start_date': {
			# The date on which the post was created
			'type': 'string',
			'format': 'partialdate',
			'nullable': True,
		},
		'end_date': {
			# The date on which the post was eliminated
			'type': 'string',
			'format': 'partialdate',
			'nullable': True,
		},
		'contact_details': {
			# Means of contacting the holder of the post
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': contact_detail_schema,
			},
			'unique_elements': True,
		},
		'links': {
			# URLs to documents about the post
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': link_schema,
			},
			'unique_elements': True,
		},
		# 'created_at' is added automatically by Eve framework
		# 'updated_at' is added automatically by Eve framework
		'sources': {
			# URLs to documents from which the post is derived
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': link_schema,
			},
			'unique_elements': True,
		},
	},
	'track_changes': ('role', 'contact_details'),
	'relations': {
		'organization': {
			# The ID of the organization in which the post is held
			'field': 'organization_id',
			'resource': 'organizations',
			'fkey': '_id'
		},
		'area': {
			# The geographic area to which this post is related
			'field': 'area_id',
			'resource': 'areas',
			'fkey': '_id'
		},
		'memberships': {
			# The memberships through which people hold the post in the organization
			'field': '_id',
			'resource': 'memberships',
			'fkey': 'post_id'
		},
	}
}


# Area
#     A geographic area whose geometry may change over time
#     JSON schema: http://popoloproject.com/schemas/area.json#
area = {
	'schema': {
		# '_id' is added automatically by Eve framework
		'name': {
			# A primary name
			'type': 'string',
			'nullable': True,
		},
		'identifier': {
			# An issued identifier
			'type': 'string',
			'nullable': True,
		},
		'classification': {
			# An area category, e.g. city
			'type': 'string',
			'nullable': True,
		},
		'parent_id': {
			# The ID of the area that contains this area
			'type': 'objectid',
			'nullable': True,
			'data_relation': {
				'resource': 'areas',
				'field': '_id',
			},
		},
		'geometry': {
			# A geometry
			'nullable': True,
		},
		# 'created_at' is added automatically by Eve framework
		# 'updated_at' is added automatically by Eve framework
		'sources': {
			# URLs to documents from which the area is derived
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': link_schema,
			},
			'unique_elements': True,
		},
	},
	'track_changes': ('name', 'geometry'),
	'relations': {
		'parent': {
			# The area that contains this area
			'field': 'parent_id',
			'resource': 'areas',
			'fkey': '_id'
		},
	}
}


# Vote
#     A voter's vote in a vote event
#     JSON schema: http://popoloproject.com/schemas/vote.json#
vote = {
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
		'party_id': {
			#The ID of the voter's political party
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
		'party': {
			# The voter's political party
			'field': 'party_id',
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


# Count
#     The number of votes for an option in a vote event
#     JSON schema: http://popoloproject.com/schemas/count.json#
count = {
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
	},
	'relations': {
		'vote_event': {
			# A vote event
			'field': 'vote_event_id',
			'resource': 'vote_events',
			'fkey': '_id'
		},
	}
}


# Vote event
#     An event at which people's votes are recorded
#     JSON schema: http://popoloproject.com/schemas/vote_event.json#
vote_event = {
	'schema': {
		# '_id' is added automatically by Eve framework
		'identifier': {
			# An issued identifier
			'type': 'string',
			'nullable': True,
		},
		'motion_id': {
			# The ID of the motion being decided
			'type': 'objectid',
			'nullable': True,
			'data_relation': {
				'resource': 'motions',
				'field': '_id',
			},
		},
		'start_date': {
			# The time at which the event begins
			'type': 'datetime',
			'nullable': True,
		},
		'end_date': {
			# The time at which the event ends
			'type': 'datetime',
			'nullable': True,
		},
		'counts': {
			# The number of votes for options
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': count['schema'],
			},
			'unique_elements': True,
		},
		'votes': {
			# Voters' votes
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': vote['schema'],
			},
			'unique_elements': True,
		},
		# 'created_at' is added automatically by Eve framework
		# 'updated_at' is added automatically by Eve framework
		'sources': {
			# URLs to documents from which the vote event is derived
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': link_schema,
			},
			'unique_elements': True,
		},
	},
	'relations': {
		'motion': {
			# The motion being decided
			'field': 'motion_id',
			'resource': 'motions',
			'fkey': '_id'
		},
	}
}


# Motion
#     A formal step to introduce a matter for consideration by an organization
#     JSON schema: http://popoloproject.com/schemas/motion.json#
motion = {
	'schema': {
		# '_id' is added automatically by Eve framework
		'organization_id': {
			# The ID of the organization in which the motion is proposed
			'type': 'objectid',
			'nullable': True,
			'data_relation': {
				'resource': 'organizations',
				'field': '_id',
			},
		},
		'context_id': {
			# The ID of the legislative context in which the motion is proposed
			'type': 'string',
			'nullable': True,
		},
		'context': {
			# The legislative context in which the motion is proposed
			'nullable': True,
		},
		'creator_id': {
			# The ID of the person who proposed the motion
			'type': 'objectid',
			'nullable': True,
			'data_relation': {
				'resource': 'people',
				'field': '_id',
			},
		},
		'text': {
			# The transcript or text of the motion
			'type': 'string',
			'nullable': True,
		},
		'object_id': {
			# The ID of a resource that the motion specifically references
			'type': 'string',
			'nullable': True,
		},
		'object': {
			# A resource that the motion specifically references
			'nullable': True,
		},
		'date': {
			# The date on which the motion was proposed
			'type': 'datetime',
			'nullable': True,
		},
		'requirement': {
			# The requirement for the motion to be adopted
			'type': 'string',
			'nullable': True,
		},
		'result': {
			# The result of the motion
			'type': 'string',
			'nullable': True,
			'allowed': ['pass', 'fail']
		},
		'vote_events': {
			# Events at which people vote on the motion
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': vote_event['schema'],
			},
			'unique_elements': True,
		},
		# 'created_at' is added automatically by Eve framework
		# 'updated_at' is added automatically by Eve framework
		'sources': {
			# URLs to documents from which the motion is derived
			'type': 'list',
			'schema': {
				'type': 'dict',
				'schema': link_schema,
			},
			'unique_elements': True,
		},
	},
	'relations': {
		'organization': {
			# The organization in which the motion is proposed
			'field': 'organization_id',
			'resource': 'organizations',
			'fkey': '_id'
		},
		'creator': {
			# The person who proposed the motion
			'field': 'creator_id',
			'resource': 'people',
			'fkey': '_id'
		},
	}
}
