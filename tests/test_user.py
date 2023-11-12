#!/bin/usr/python3
"""testing user"""
import unittest
from time import sleep
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
import re


class TestUser(unittest.TestCase):
	'''testUser class'''
	def test_valid_email(self):
		'''test email'''
		pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
		user = User()
		self.assertIsInstance(user, BaseModel)
		self.assertIsInstance(user, User)
		self.assertTrue(hasattr(user, 'email'))
		# user_email = user.email
		# self.assertTrue(pattern.match(user_email))
		user_email2 = 'email@email@com'
		user_email3 = 'invalid_email'
		self.assertFalse(pattern.match(user_email2))
		self.assertFalse(pattern.match(user_email3))

	def test_valid_name(self):
		'''test name'''
		user = User()
		self.assertTrue(hasattr(user, 'first_name'))
		self.assertTrue(hasattr(user, 'last_name'))
		self.assertIsInstance(user.first_name, str)
		self.assertIsInstance(user.last_name, str)
		self.assertEqual(user.first_name, "")
		self.assertEqual(user.last_name, "")

	def test_password(self):
		'''test password '''
		user = User()
		self.assertTrue(hasattr(user, "password"))
		self.assertEqual(user.password, "")
