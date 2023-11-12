#!/bin/usr/python3
"""testing 	"""
import unittest
from models.base_model import BaseModel
from models.state import State
import re


class TestUser(unittest.TestCase):
	'''testUser class'''

	def test_valid_name(self):
		'''test name'''
		state = State()
		self.assertTrue(hasattr(state, 'name'))
		self.assertEqual(state.name, '')
