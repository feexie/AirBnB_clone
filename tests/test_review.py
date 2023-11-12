#!/bin/usr/python3
"""testing 	"""
import unittest
from models.base_model import BaseModel
from models.review import Review
import re


class TestUser(unittest.TestCase):
	'''review class'''
	def test_valid_place_id(self):
		'''test place_id'''
		review = Review()
		self.assertTrue(hasattr(review, "place_id"))
		self.assertEqual(type(review.place_id), str)
		self.assertEqual(review.place_id, "")

	def test_valid_text(self):
		'''test name'''
		review = Review()
		self.assertTrue(hasattr(review, 'text'))
		self.assertEqual(type(review.text), str)
		self.assertEqual(review.text, '')
	
	def test_valid_user_id(self):
		'''test user_id'''
		review = Review()
		self.assertTrue(hasattr(review, 'user_id'))
		self.assertEqual(type(review.user_id), str)
		self.assertEqual(review.user_id, '')
