from domain import *

# Common settings for all applications corresponding to individual parliaments
common = {
	'DEBUG': True,

	'MONGO_HOST': 'localhost',
	'MONGO_PORT': 27017,

	'RESOURCE_METHODS': ['GET', 'POST', 'DELETE'],
	'ITEM_METHODS': ['GET', 'PATCH', 'PUT', 'DELETE'],
	'PUBLIC_METHODS': ['GET'],
	'PUBLIC_ITEM_METHODS': ['GET'],

	'IF_MATCH': False,

	'DATE_FORMAT': '%Y-%m-%d %H:%M:%S',

	'LAST_UPDATED': 'updated_at',
	'DATE_CREATED': 'created_at',

	'CACHE_CONTROL': 'public, max-age=300',
	'CACHE_EXPIRES': 300,

	'FILES_SERVER': 'http://files.parldata.eu',
	'FILES_DIR': '../files.parldata.eu',

	'DOMAIN': {
		'people': person,
		'organizations': organization,
		'memberships': membership,
		'posts': post,
	},
}

common['DOMAIN']['people']['item_title'] = 'person'
