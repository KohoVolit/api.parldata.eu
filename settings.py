from schemas import person, organization, membership, post, area, motion, vote_event, vote, speech, log

# Common settings for all applications corresponding to individual parliaments
common = {
	'DEBUG': True,

	'MONGO_HOST': 'localhost',
	'MONGO_PORT': 27017,
	'MONGO_QUERY_BLACKLIST': ['$where'],	# allows $regex operator in queries
	
	'RESOURCE_METHODS': ['GET', 'POST', 'DELETE'],
	'ITEM_METHODS': ['GET', 'PATCH', 'PUT', 'DELETE'],
	'PUBLIC_METHODS': ['GET'],
	'PUBLIC_ITEM_METHODS': ['GET'],

	'IF_MATCH': False,

	'DATE_FORMAT': '%Y-%m-%d %H:%M:%S',

	'ID_FIELD': 'id',
	'ITEM_LOOKUP_FIELD': 'id',
	'ITEM_URL': 'string',
	'LAST_UPDATED': 'updated_at',
	'DATE_CREATED': 'created_at',

	'CACHE_CONTROL': 'public, max-age=300',
	'CACHE_EXPIRES': 300,

	'FILES_SERVER': 'http://files.parldata.eu',
	'FILES_DIR': '../files.parldata.eu',

	'DOMAIN': {
		'people': person.resource,
		'organizations': organization.resource,
		'memberships': membership.resource,
		'posts': post.resource,
		'areas': area.resource,
		'motions': motion.resource,
		'vote_events': vote_event.resource,
		'votes': vote.resource,
		'speeches': speech.resource,
		'logs': log.resource,
	},
}

common['DOMAIN']['people']['item_title'] = 'person'
common['DOMAIN']['people']['item_title'] = 'speech'
common['DOMAIN']['vote_events']['url'] = 'vote-events'
