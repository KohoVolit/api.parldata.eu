# -*- coding: UTF-8 -*-

DEBUG = True

SERVER_NAME = 'localhost:5000'

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'vpapi-dev'
MONGO_USERNAME = 'vpapi'
MONGO_PASSWORD = 'vpapi'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
PUBLIC_METHODS = ['GET']
PUBLIC_ITEM_METHODS = ['GET']

AUTHORIZED_USERS = [
	('updater', 'secret')
]

IF_MATCH = False

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

LAST_UPDATED = 'updated_at'
DATE_CREATED = 'created_at'

CACHE_CONTROL = 'public, max-age=300'
CACHE_EXPIRES = 300

FILES_SERVER = SERVER_NAME.replace('api.', 'http://files.')
FILES_DIR = 'files'

from domain import *

DOMAIN = {
	'people': {
		'schema': person,
		'item_title': 'person',
		'track_changes': person_track_changes,
		'save_files': person_save_files
	},
	'organizations': {
		'schema': organization,
		'track_changes': organization_track_changes,
		'save_files': organization_save_files
	},
	'memberships': {
		'schema': membership
	},
	# 'posts': { 'schema': post },
}
