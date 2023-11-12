#!/bin/usr/python3
"""testing 	"""
import unittest
from time import sleep
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity
import re


class TestUser(unittest.TestCase):
	'''testUser class'''

	def test_valid_name(self):
		'''test name'''
		amenity = Amenity()
		self.assertTrue(hasattr(amenity, 'name'))
		self.assertEqual(type(amenity.name), str)
		self.assertEqual(amenity.name, '')
