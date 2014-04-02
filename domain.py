# -*- coding: UTF-8 -*-

# Identifier
# 	An issued identifier
# 	JSON schema: http://popoloproject.com/schemas/identifier.json#
identifier = {
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
# 	A URL
# 	JSON schema: http://popoloproject.com/schemas/link.json#
link = {
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
# 	An alternate or former name
# 	JSON schema: http://popoloproject.com/schemas/other_name.json#
other_name = {
	'name': {
		# An alternate or former name
		'type': 'string',
		'required': True,
		'empty': False,
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
# 	A means of contacting an entity
# 	JSON schema: http://popoloproject.com/schemas/contact_detail.json#
contact_detail = {
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
	'sources': {
		# URLs to documents from which the contact detail is derived
		'type': 'list',
		'schema': {
			'type': 'dict',
			'schema': link,
		},
		'unique_elements': True,
	},
}

# Person
# 	A real person, alive or dead
# 	JSON schema: http://popoloproject.com/schemas/person.json#
person = {
	# 'id' is added automatically by Eve framework
	'name': {
		# A person's preferred full name
		'type': 'string',
		'required': True,
		'empty': False,
	},
	'other_names': {
		# Alternate or former names
		'type': 'list',
		'schema': {
			'type': 'dict',
			'schema': other_name,
		},
		'unique_elements': True,
	},
	'identifiers': {
		# Issued identifiers
		'type': 'list',
		'schema': {
			'type': 'dict',
			'schema': identifier,
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
			'schema': contact_detail,
		},
		'unique_elements': True,
	},
	'links': {
		# URLs to documents about the person
		'type': 'list',
		'schema': {
			'type': 'dict',
			'schema': link,
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
			'schema': link,
		},
		'unique_elements': True,
	},
	'changes': {
		# List of property value changes
		# Managed automatically by on_insert hook when tracked properties change value
		'type': 'list',
	},
}
person_track_changes = ('honorific_prefix', 'honorific_suffix', 'email', 'gender', 'image', 'national_identity', 'contact_details')
person_save_files = ('image', )

# Organization
# 	A group with a common purpose or reason for existence that goes beyond the set of people belonging to it
# 	JSON schema: http://popoloproject.com/schemas/organization.json#
organization = {
	# 'id' is added automatically by Eve framework
	'name': {
		# A primary name, e.g. a legally recognized name
		'type': 'string',
		'required': True,
		'empty': False,
	},
	'other_names': {
		# Alternate or former names
		'type': 'list',
		'schema': {
			'type': 'dict',
			'schema': other_name,
		},
		'unique_elements': True,
	},
	'identifiers': {
		# Issued identifiers
		'type': 'list',
		'schema': {
			'type': 'dict',
			'schema': identifier,
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
			'schema': contact_detail,
		},
		'unique_elements': True,
	},
	'links': {
		# URLs to documents about the organization
		'type': 'list',
		'schema': {
			'type': 'dict',
			'schema': link,
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
			'schema': link,
		},
		'unique_elements': True,
	},
	'changes': {
		# List of property value changes
		# Managed automatically by on_insert hook when tracked properties change value
		'type': 'list',
	},
}
organization_track_changes = ('image', 'contact_details')
organization_save_files = ('image', )

# Membership
# 	A relationship between a person and an organization
# 	JSON schema: http://popoloproject.com/schemas/membership.json#
membership = {
	# 'id' is added automatically by Eve framework
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
	'on_behalf_of_id': {
		# The ID of the organization on whose behalf the person is a party to the relationship
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
	'contact_details': {	# remove ???
		# Means of contacting the person who is a party to the relationship
		'type': 'list',
		'schema': {
			'type': 'dict',
			'schema': contact_detail,
		},
		'unique_elements': True,
	},
	'links': {
		# URLs to documents about the membership
		'type': 'list',
		'schema': {
			'type': 'dict',
			'schema': link,
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
			'schema': link,
		},
		'unique_elements': True,
	},
}


##############################################################33
#
# # Post
# # 	A position that exists independent of the person holding it
# # 	JSON schema: http://popoloproject.com/schemas/post.json#
# post = {
	# # 'id' is added automatically by Eve framework
	# 'label': {
		# # 'A label describing the post
		# 'type': 'string',
		# 'required': True
	# },
	# 'role': {
		# # 'The function that the holder of the post fulfills
		# 'type': 'string',
		# 'nullable': True,
	# },
	# 'organization_id': {
		# # 'The ID of the organization in which the post is held
		# 'type': 'objectid',
		# 'nullable': True,
		# 'data_relation': {
			# 'resource': 'organizations',
			# 'field': '_id',
		 # },
	# },
	# 'start_date': {
		# # 'The date on which the post was created
		# 'type': 'string',
		# 'format': 'partialdate',
		# 'nullable': True,
	# },
	# 'end_date': {
		# # 'The date on which the post was eliminated
		# 'type': 'string',
		# 'format': 'partialdate',
		# 'nullable': True,
	# },
	# 'contact_details': {
		# # 'Means of contacting the holder of the post
		# 'type': 'list',
		# 'schema': {
			# 'type': 'dict',
			# 'schema': contact_detail,
		# },
		# 'unique_elements': True,
	# },
	# 'links': {
		# # 'URLs to documents about the post
		# 'type': 'list',
		# 'schema': {
			# 'type': 'dict',
			# 'schema': link,
		# },
		# 'unique_elements': True,
	# },
	# # 'created_at' is added automatically by Eve framework
	# # 'updated_at' is added automatically by Eve framework
	# 'sources': {
		# # 'URLs to documents from which the post is derived
		# 'type': 'list',
		# 'schema': {
			# 'type': 'dict',
			# 'schema': link,
		# },
		# 'unique_elements': True,
	# },
# }
