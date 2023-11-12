#!/usr/bin/python3
""" BaseModel tests"""
from datetime import datetime
import models
from time import sleep
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
	'''BaseModel testing'''

	def test_uuid(self):
		"""test uuid"""
		bm1 = BaseModel()
		bm2 = BaseModel()
		self.assertIsInstance(bm1, BaseModel)
		self.assertTrue(hasattr(bm1, 'id'))
		self.assertTrue(hasattr(bm2, 'id'))
		self.assertNotEqual(bm1.id, bm2.id)
		self.assertIsInstance(bm1.id, str)
		self.assertIsInstance(bm2.id, str)
	
	def test_time(self):
		"""test timme"""
		cr_at = datetime.today()
		bm = BaseModel()
		up_at = datetime.today()
		self.assertIsInstance(bm, BaseModel)
		self.assertTrue(hasattr(bm, 'created_at'))
		self.assertTrue(hasattr(bm, 'updated_at'))
		self.assertTrue(cr_at <= bm.created_at and bm.created_at <= up_at)
		bm2 = BaseModel()
		self.assertNotEqual(bm.created_at, bm2.updated_at)


	def test_dict(self):
		"""test dict """
		md = BaseModel()
		md.name = "Hbnb"
		md.my_number = 89
		d = md.to_dict()
		attrs = ["id",
						  "created_at",
						  "updated_at",
						  "name",
						  "my_number",
						  "__class__"]
		self.assertCountEqual(d.keys(), attrs)
		self.assertEqual(d['__class__'], 'BaseModel')
		self.assertEqual(d['name'], "Hbnb")
		self.assertEqual(d['my_number'], 89)

	def test_correct_values(self):
		"""test values """
		time_format = "%Y-%m-%dT%H:%M:%S.%f"
		bm = BaseModel()

		self.assertIsInstance(bm, BaseModel)
		self.assertTrue(hasattr(bm, 'updated_at'))
		self.assertTrue(hasattr(bm, 'created_at'))

	def test_str(self):
		"""test str"""
		bm = BaseModel()
		string = "[BaseModel] ({}) {}".format(bm.id, bm.__dict__)
		self.assertEqual(string, str(bm))

	def test_save(self):
		bm = BaseModel()
		sleep(0.05)
		old_updated_at = bm.updated_at
		bm.save()
		self.assertLess(old_updated_at, bm.updated_at)
		bm2 = BaseModel()
		old_updated_at = bm2.updated_at
		bm.save()
		new_updated_at = bm2.updated_at
		self.assertEqual(old_updated_at, new_updated_at)
