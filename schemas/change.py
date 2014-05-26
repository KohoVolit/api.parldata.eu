""" Change
	An entry in API managed list of changes of entity's property values
	Not part of Popolo standard
"""

schema = {
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
