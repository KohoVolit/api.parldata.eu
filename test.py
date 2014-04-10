#!/usr/bin/env python3

"""Unit tests to test API functionality."""

import unittest
from datetime import datetime, date, timedelta
import glob
import requests.exceptions
import vpapi


def datestring_add(datestring, days):
	"""Returns the date specified as string in ISO format with given number of days added.
	"""
	return (datetime.strptime(datestring, '%Y-%m-%d') + timedelta(days=days)).date().isoformat()


class TestBasicFeatures(unittest.TestCase):
	def setUp(self):
		vpapi.parliament('xx/test')
		vpapi.deauthorize()

	def test_parliament_endpoint(self):
		"""request to root endpoint of the API should return list of 3 resources"""
		result = vpapi.get('')
		self.assertEqual(len(result['_links']['child']), 3)

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

	def setUp(self):
		# authorize to xx/test parliament and ensure exactly one person with the sample value
		vpapi.parliament('xx/test')
		vpapi.authorize('xx/test', 'secret')
		vpapi.delete('people', where={'identifiers': {'$elemMatch': self.sample_identifier}})
		result = vpapi.post('people', self.sample_person)
		self.person_id = result['id']

	def test_validation_of_disjointness(self):
		"""inserting of another entity containing identical identifier to an existing one should return `ERR` status"""
		result = vpapi.post('people', self.sample_person)
		self.assertEqual(result['_status'], 'ERR')

	def test_validation_of_unique_elements(self):
		"""inserting of duplicate element into the list of links should raise HTTPError"""
		result = vpapi.patch(
			'people' + '/' + self.person_id,
			{'links': [self.sample_link, self.sample_link]})
		self.assertEqual(result['_status'], 'ERR')

	def test_id_field_renaming(self):
		"""entity should have an `id` field instead of `_id`"""
		result = vpapi.get('people' + '/' + self.person_id)
		self.assertIn('id', result)
		self.assertNotIn('_id', result)

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
			'people' + '/' + self.person_id,
			modified)
		expected_change = {
			'property': 'email',
			'value': 'jqpublic@xyz.example.com',
			'end_date': datestring_add(date.today().isoformat(), -1)
		}
		result = vpapi.get('people' + '/' + self.person_id)
		self.assertIn('changes', result)
		self.assertEqual(len(result['changes']), 2)
		self.assertEqual(expected_change, result['changes'][0])
		self.assertEqual(explicit_change, result['changes'][1])

	def test_changes_on_patch(self):
		"""changed value in any of the fields with tracked history should be logged	into the `changes` field with `end_date` equal to yesterday. Explicitly sent changes should be merged with the automatically managed ones."""
		explicit_change = {
			'property': 'abc',
			'value': 'xyz'
		}
		vpapi.patch(
			'people' + '/' + self.person_id,
			{'email': 'new@example.com', 'changes': [explicit_change]})
		expected_change = {
			'property': 'email',
			'value': 'jqpublic@xyz.example.com',
			'end_date': datestring_add(date.today().isoformat(), -1)
		}
		result = vpapi.get('people' + '/' + self.person_id)
		self.assertIn('changes', result)
		self.assertEqual(len(result['changes']), 2)
		self.assertEqual(expected_change, result['changes'][0])
		self.assertEqual(explicit_change, result['changes'][1])

	def test_changes_on_put_with_effective_date(self):
		"""if parameter `effective_date` is sent in URL query string then the change should be assumed at the given date and not today"""
		modified = self.sample_person.copy()
		modified['email'] = 'new@example.com'
		vpapi.put(
			'people' + '/' + self.person_id,
			modified,
			effective_date='2000-01-01')
		expected_change = {
			'property': 'email',
			'value': 'jqpublic@xyz.example.com',
			'end_date': '1999-12-31'
		}
		result = vpapi.get('people' + '/' + self.person_id)
		self.assertIn(expected_change, result.get('changes'))

	def test_changes_on_patch_with_effective_date(self):
		"""if parameter `effective_date` is sent in URL query string then the change should be assumed at the given date and not today"""
		vpapi.patch(
			'people' + '/' + self.person_id,
			{'email': 'new@example.com'},
			effective_date='2000-01-01')
		expected_change = {
			'property': 'email',
			'value': 'jqpublic@xyz.example.com',
			'end_date': '1999-12-31'
		}
		result = vpapi.get('people' + '/' + self.person_id)
		self.assertIn(expected_change, result.get('changes'))

	def test_fix_on_put(self):
		"""if parameter `effective_date` in URL query string has value `fix`, the change should not be logged into the `changes` field"""
		modified = self.sample_person.copy()
		modified['email'] = 'new@example.com'
		vpapi.put(
			'people' + '/' + self.person_id,
			modified,
			effective_date='fix')
		result = vpapi.get('people' + '/' + self.person_id)
		self.assertNotIn('changes', result)

	def test_fix_on_patch(self):
		"""if parameter `effective_date` in URL query string has value `fix`, the change should not be logged into the `changes` field"""
		vpapi.patch(
			'people' + '/' + self.person_id,
			{'email': 'new@example.com'},
			effective_date='fix')
		result = vpapi.get('people' + '/' + self.person_id)
		self.assertNotIn('changes', result)

	def test_file_mirroring(self):
		"""URLs in the mirrored fields should be relocated and the referenced files downloaded"""
		# check that the file has been relocated and downloaded
		mirrored_url = 'http://files.parldata.eu/xx/test/people/' + self.person_id + '/image.png'
		pathfile = '../files.parldata.eu/xx/test/people/' + self.person_id + '/image'
		result = vpapi.get('people' + '/' + self.person_id)
		self.assertEqual(result['image'], mirrored_url)
		self.assertEqual(len(glob.glob(pathfile + '.*')), 1)

		# check that the file is not mirrored again if the source hasn't changed
		vpapi.patch('people' + '/' + self.person_id, {'image': self.sample_image_url})
		result = vpapi.get('people' + '/' + self.person_id)
		self.assertEqual(result['image'], mirrored_url)
		self.assertEqual(len(glob.glob(pathfile + '.*')), 1)

		# check that new file is mirrored if the source file changes
		new_image = 'http://www.bing.com/s/a/hpc12.png'
		vpapi.patch('people' + '/' + self.person_id, {'image': new_image})
		result = vpapi.get('people' + '/' + self.person_id)
		self.assertEqual(result['image'], mirrored_url.replace('.png', '.2.png'))
		self.assertEqual(len(glob.glob(pathfile + '.*')), 2)

if __name__ == '__main__':
	unittest.main()
