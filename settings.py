from schemas import person, organization, membership, post
from schemas import motion, vote_event, vote
from schemas import area
from schemas import speech
from schemas import event
from schemas import log

# Common settings for all applications corresponding to individual parliaments
common = {
	'DEBUG': True,

	'MONGO_HOST': 'localhost',
	'MONGO_PORT': 27017,

	# allow $regex operator in queries
	'MONGO_QUERY_BLACKLIST': ['$where'],
	
	'RESOURCE_METHODS': ['GET', 'POST', 'DELETE'],
	'ITEM_METHODS': ['GET', 'PATCH', 'PUT', 'DELETE'],
	'PUBLIC_METHODS': ['GET'],
	'PUBLIC_ITEM_METHODS': ['GET'],

	'IF_MATCH': False,

	# ISO 8601 date format (example: 2014-12-31T12:34:56)
	'DATE_FORMAT': '%Y-%m-%dT%H:%M:%S',

	'ID_FIELD': 'id',
	'ITEM_LOOKUP_FIELD': 'id',
	'ITEM_URL': 'string',
	'LAST_UPDATED': 'updated_at',
	'DATE_CREATED': 'created_at',

	'CACHE_CONTROL': 'public, max-age=300',
	'CACHE_EXPIRES': 300,

	'FILES_HOST': 'http://files.parldata.eu',
	'FILES_DIR': '../files.parldata.eu',

	'X_DOMAINS': '*',

	'DOMAIN': {
		'people': person.resource,
		'organizations': organization.resource,
		'memberships': membership.resource,
		'posts': post.resource,
		'motions': motion.resource,
		'vote_events': vote_event.resource,
		'votes': vote.resource,
		'areas': area.resource,
		'speeches': speech.resource,
		'events': event.resource,
		'logs': log.resource,
	},
}

common['DOMAIN']['people']['item_title'] = 'person'
common['DOMAIN']['speeches']['item_title'] = 'speech'
common['DOMAIN']['vote_events']['url'] = 'vote-events'

for resource in common['DOMAIN'].values():
	resource['query_objectid_as_string'] = True
