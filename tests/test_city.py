#!/bin/usr/python3
"""testing 	"""
import unittest
from time import sleep
from datetime import datetime
from models.base_model import BaseModel
from models.city import City
import re


class TestUser(unittest.TestCase):
	'''testUser class'''
	def test_valid_state_id(self):
		'''test state_id'''
		city = City()
		self.assertTrue(hasattr(city, "state_id"))
		self.assertEqual(city.state_id, "")


	def test_valid_name(self):
		'''test name'''
		city = City()
		self.assertTrue(hasattr(city, 'name'))
		self.assertEqual(city.name, '')
