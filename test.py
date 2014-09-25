#!/usr/bin/env python3

"""Unit tests to test API functionality."""

import unittest
from datetime import datetime, date, timedelta
import glob
import requests.exceptions
from client import vpapi


def datestring_add(datestring, days):
	"""Returns the date specified as string in ISO format with given number of days added.
	"""
	return (datetime.strptime(datestring, '%Y-%m-%d') + timedelta(days=days)).date().isoformat()


class TestBasicFeatures(unittest.TestCase):
	def setUp(self):
		vpapi.parliament('xx/example')
		vpapi.deauthorize()

	def test_parliament_endpoint(self):
		"""request to root endpoint of the API should return list of 9 resources"""
		result = vpapi.get('')
		self.assertEqual(len(result['_links']['child']), 9)

	def test_nonexistent_endpoint(self):
		"""request to a non-existent API endpoint should raise HTTPError"""
		self.assertRaises(requests.exceptions.HTTPError, vpapi.get, 'non-existent')

	def test_missing_authorization(self):
		"""data modifying request without authorization should raise HTTPError"""
		self.assertRaises(requests.exceptions.HTTPError, vpapi.post, 'people', {'name': 'abc'})


class TestAdvancedFeatures(unittest.TestCase):
	sample_identifier = {
		'identifier': '046454286',
		'scheme': 'SIN'
	}
	sample_link = {
		'url': 'http://en.wikipedia.org/wiki/John_Q._Public',
		'note': 'Wikipedia page'
	}
	sample_image_url = 'http://www.google.com/images/srpr/logo11w.png'
	sample_person = {
		'name': 'Mr. John Q. Public, Esq.',
		'identifiers': [
			sample_identifier
		],
		'email': 'jqpublic@xyz.example.com',
		'gender': 'male',
		'birth_date': '1920-01',
		'death_date': '2010-01-01',
		'image': sample_image_url,
		'summary': 'A hypothetical member of society deemed a "common man"',
		'biography': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...',
		'national_identity': 'Scottish',
		'contact_details': [
			{
				'label': 'Mobile number',
				'type': 'tel',
				'value': '+1-555-555-0100',
				'note': 'Free evenings and weekends'
			}
		],
		'links': [
			sample_link
		]
	}
	person_with_id = {
		'id': 'bilbo-baggins',
		'name': 'Bilbo Baggins',
	}
	sample_organization = {
		"name": "ABC, Inc.",
		"founding_date": "1950-01-01",
		"dissolution_date": "2000-01-01",
	}
	sample_membership = {
		"label": "Kitchen assistant at ABC, Inc.",
		"role": "Kitchen assistant",
		"start_date": "1970-01",
		"end_date": "1971-12-31",
	}

	def setUp(self):
		# authorize to xx/example parliament
		vpapi.parliament('xx/example')
		vpapi.authorize('scraper', 'secret')

		# ensure exactly one person with the sample value
		result = vpapi.get('people', where={'identifiers': {'$elemMatch': self.sample_identifier}})
		if result['_items']:
			vpapi.delete('people/%s' % result['_items'][0]['id'])
		result = vpapi.post('people', self.sample_person)
		self.person_id = result['id']
		# and no person with specified id
		result = vpapi.get('people', where={'id': self.person_with_id['id']})
		if result['_items']:
			vpapi.delete('people/%s' % self.person_with_id['id'])

		# ensure exactly one organization with the sample value
		result = vpapi.get('organizations', where={'name': 'ABC, Inc.'})
		if result['_items']:
			vpapi.delete('organizations/%s' % result['_items'][0]['id'])
		result = vpapi.post('organizations', self.sample_organization)
		self.organization_id = result['id']

		# ensure exactly one membership with the sample value
		result = vpapi.get('memberships', where={'label': 'Kitchen assistant at ABC, Inc.'})
		if result['_items']:
			vpapi.delete('memberships/%s' % result['_items'][0]['id'])
		self.sample_membership['person_id'] = self.person_id
		self.sample_membership['organization_id'] = self.organization_id
		result = vpapi.post('memberships', self.sample_membership)
		self.membership_id = result['id']

	def tearDown(self):
		# remove entities and files created for testing
		try:
			vpapi.delete('people/%s' % self.person_id)
			vpapi.delete('organizations/%s' % self.organization_id)
			vpapi.delete('memberships/%s' % self.membership_id)
		except requests.exceptions.HTTPError:
			pass

	def test_validation_of_disjointness(self):
		"""inserting of another entity containing identical identifier to an existing one should raise HTTPError"""
		self.assertRaises(requests.exceptions.HTTPError, vpapi.post, 'people', self.sample_person)

	def test_validation_of_unique_elements(self):
		"""inserting of duplicate element into the list of links should raise HTTPError"""
		resource = 'people/%s' % self.person_id
		updates = {'links': [self.sample_link, self.sample_link]}
		self.assertRaises(requests.exceptions.HTTPError, vpapi.patch, resource, updates)

	def test_id_field(self):
		"""entity should use `id` instead of `_id`"""
		result = vpapi.get('people/%s' % self.person_id)
		self.assertIn('id', result)
		self.assertNotIn('_id', result)
		result = vpapi.post('people', self.person_with_id)
		self.assertIn('id', result)
		self.assertNotIn('_id', result)
		self.assertEqual(result['id'], self.person_with_id['id'])
		result = vpapi.patch('people/%s' % result['id'], {'id': 'abc'})
		self.assertEqual(result['id'], 'abc')
		vpapi.delete('people/%s' % self.person_with_id['id'])

	def test_changes_on_put(self):
		"""changed value in any of the fields with tracked history should be logged	into the `changes` field with `end_date` equal to yesterday. Explicitly sent changes should be merged with the automatically managed ones."""
		modified = self.sample_person.copy()
		modified['email'] = 'new@example.com'
		explicit_change = {
			'property': 'abc',
			'value': 'xyz'
		}
		modified['changes'] = [explicit_change]
		vpapi.put(
			'people/%s' % self.person_id,
			modified)
		expected_change = {
			'property': 'email',
			'value': 'jqpublic@xyz.example.com',
			'end_date': datestring_add(date.today().isoformat(), -1)
		}
		result = vpapi.get('people/%s' % self.person_id)
		self.assertIn('changes', result)
		self.assertEqual(len(result['changes']), 2)
		self.assertEqual(expected_change, result['changes'][0])
		self.assertEqual(explicit_change, result['changes'][1])

	def test_changes_on_patch(self):
		"""changed value in any of the fields with tracked history should be logged into the `changes` field with `end_date` equal to yesterday. Explicitly sent changes should be merged with the automatically managed ones."""
		explicit_change = {
			'property': 'abc',
			'value': 'xyz'
		}
		vpapi.patch(
			'people/%s' % self.person_id,
			{'email': 'new@example.com', 'changes': [explicit_change]})
		expected_change = {
			'property': 'email',
			'value': 'jqpublic@xyz.example.com',
			'end_date': datestring_add(date.today().isoformat(), -1)
		}
		result = vpapi.get('people/%s' % self.person_id)
		self.assertIn('changes', result)
		self.assertEqual(len(result['changes']), 2)
		self.assertEqual(expected_change, result['changes'][0])
		self.assertEqual(explicit_change, result['changes'][1])

	def test_changes_on_put_with_effective_date(self):
		"""if parameter `effective_date` is sent in URL query string then the change should be assumed at the given date and not today"""
		modified = self.sample_person.copy()
		modified['email'] = 'new@example.com'
		vpapi.put(
			'people/%s' % self.person_id,
			modified,
			effective_date='2000-01-01')
		expected_change = {
			'property': 'email',
			'value': 'jqpublic@xyz.example.com',
			'end_date': '1999-12-31'
		}
		result = vpapi.get('people/%s' % self.person_id)
		self.assertIn(expected_change, result.get('changes'))

	def test_changes_on_patch_with_effective_date(self):
		"""if parameter `effective_date` is sent in URL query string then the change should be assumed at the given date and not today"""
		vpapi.patch(
			'people/%s' % self.person_id,
			{'email': 'new@example.com'},
			effective_date='2000-01-01')
		expected_change = {
			'property': 'email',
			'value': 'jqpublic@xyz.example.com',
			'end_date': '1999-12-31'
		}
		result = vpapi.get('people/%s' % self.person_id)
		self.assertIn(expected_change, result.get('changes'))

	def test_fix_on_put(self):
		"""if parameter `effective_date` in URL query string has value `fix`, the change should not be logged into the `changes` field"""
		modified = self.sample_person.copy()
		modified['email'] = 'new@example.com'
		vpapi.put(
			'people/%s' % self.person_id,
			modified,
			effective_date='fix')
		result = vpapi.get('people/%s' % self.person_id)
		self.assertNotIn('changes', result)

	def test_fix_on_patch(self):
		"""if parameter `effective_date` in URL query string has value `fix`, the change should not be logged into the `changes` field"""
		vpapi.patch(
			'people/%s' % self.person_id,
			{'email': 'new@example.com'},
			effective_date='fix')
		result = vpapi.get('people/%s' % self.person_id)
		self.assertNotIn('changes', result)

	def test_file_mirroring(self):
		"""URLs in the mirrored fields should be relocated and the referenced files downloaded"""
		# check that the file has been relocated and downloaded
		mirrored_url = 'http://files.parldata.eu/xx/example/people/%s/image.png' % self.person_id
		pathfile = '../files.parldata.eu/xx/example/people/%s/image' % self.person_id
		result = vpapi.get('people/%s' % self.person_id)
		self.assertEqual(result['image'], mirrored_url)
		self.assertEqual(len(glob.glob(pathfile + '.*')), 1)

		# check that the file is not mirrored again if the source hasn't changed
		vpapi.patch('people/%s' % self.person_id, {'image': self.sample_image_url})
		result = vpapi.get('people/%s' % self.person_id)
		self.assertEqual(result['image'], mirrored_url)
		self.assertEqual(len(glob.glob(pathfile + '.*')), 1)

		# check that new file is mirrored if the source file changes
		new_image = 'http://upload.wikimedia.org/wikipedia/en/b/bc/Wiki.png'
		vpapi.patch('people/%s' % self.person_id, {'image': new_image})
		result = vpapi.get('people/%s' % self.person_id)
		self.assertEqual(result['image'], mirrored_url.replace('.png', '.2.png'))
		self.assertEqual(len(glob.glob(pathfile + '.*')), 2)

		# check that mirrored files are deleted with entity deletion
		vpapi.delete('people/%s' % self.person_id)
		self.assertEqual(len(glob.glob(pathfile + '.*')), 0)

	def test_embedding(self):
		"""related entities specified in URL query parameter `embed` should be embedded in to the returned document"""
		# check two-level embedding
		result = vpapi.get('people/%s?embed=["memberships.organization"]' % self.person_id)
		self.assertIn('memberships', result)
		self.assertIsInstance(result['memberships'], list)
		self.assertIsInstance(result['memberships'][0], dict)
		self.assertNotIn('person_id', result['memberships'][0])
		self.assertIn('organization', result['memberships'][0])
		self.assertNotIn('organization_id', result['memberships'][0])
		self.assertIsInstance(result['memberships'][0]['organization'], dict)

		# check that an entity is not embedded recursively
		result = vpapi.get('people/%s?embed=["memberships.person"]' % self.person_id)
		self.assertIn('memberships', result)
		self.assertIsInstance(result['memberships'], list)
		self.assertIsInstance(result['memberships'][0], dict)
		self.assertNotIn('person_id', result['memberships'][0])
		self.assertNotIn('person', result['memberships'][0])
		self.assertIn('organization_id', result['memberships'][0])


if __name__ == '__main__':
	unittest.main()
