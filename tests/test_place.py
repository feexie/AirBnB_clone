#!/bin/usr/python3
"""testing 	"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestUser(unittest.TestCase):
	'''testUser class'''
	def test_city_id(self):
		'''test state_id'''
		place = Place()
		self.assertTrue(hasattr(place, "city_id"))
		self.assertEqual(place.city_id, "")
		self.assertEqual(type(place.city_id), str)

	def test_valid_name(self):
		'''test name'''
		place = Place()
		self.assertTrue(hasattr(place, 'name'))
		self.assertIsInstance(place.name, str)
		self.assertEqual(type(place.name), str)

	def test_user_id(self):
		'''test user_id'''
		place = Place()
		self.assertTrue(hasattr(place, "user_id"))
		self.assertEqual(place.user_id, "")
		self.assertEqual(type(place.user_id), str)

	def test_description(self):
		'''test description'''
		place = Place()
		self.assertTrue(hasattr(place, "description"))
		self.assertEqual(place.description, "")
		self.assertEqual(type(place.description), str)
	
	def test_rooms(self):
		'''test rooms'''
		place = Place()
		self.assertTrue(hasattr(place, "number_room"))
		self.assertEqual(place.number_room, 0)
		self.assertEqual(type(place.number_room), int)

	def test_bathrooms(self):
		'''test bathrooms'''
		place = Place()
		self.assertTrue(hasattr(place, "number_bathrooms"))
		self.assertEqual(place.number_bathrooms, 0)
		self.assertEqual(type(place.number_bathrooms), int)

	def test_max_guest(self):
		'''test max_guest'''
		place = Place()
		self.assertTrue(hasattr(place, "max_guest"))
		self.assertEqual(place.max_guest, 0)
		self.assertEqual(type(place.max_guest), int)

	def test_price_by_night(self):
		'''test price_by_night'''
		place = Place()
		self.assertTrue(hasattr(place, "price_by_night"))
		self.assertEqual(place.price_by_night, 0)
		self.assertEqual(type(place.price_by_night), int)

	def test_latitude(self):
		'''test latitude'''
		place = Place()
		self.assertTrue(hasattr(place, "latitude"))
		self.assertEqual(place.latitude, 0.0)
		self.assertEqual(type(place.latitude), float)

	def test_longitude(self):
		'''test longitude'''
		place = Place()
		self.assertTrue(hasattr(place, "longitude"))
		self.assertEqual(place.longitude, 0.0)
		self.assertEqual(type(place.longitude), float)
	
	def test_amenity_ids(self):
		'''test amenity_ids'''
		place = Place()
		self.assertTrue(hasattr(place, "amenity_ids"))
		self.assertEqual(place.amenity_ids, [])
		self.assertEqual(type(place.amenity_ids), list)
