#!/usr/bin/python3
""" FileStorage class """


import json
import os
from models.base_model import BaseModel

class FileStorage:
	"""
	serializes instances to a JSON file and deserializes
	JSON file to instances:
	"""


	__file_path = "file.json"
	__objects = {}

	def all(self):
		''' returns objects '''

		return (self.__objects)

	def new(self, obj):
		''' set new object '''
		if obj:
			className = obj.__class__.__name__
			obj_key = className + '.' + obj.id
			self.__objects[obj_key] = obj

	def save(self):
		''' serialize to JSON file '''

		# print('saving...\n')
		json_file_objects = {}
		for k in self.__objects:
			json_file_objects[k] = self.__objects[k].to_dict()
		
		with open(FileStorage.__file_path, 'w') as path:
			json.dump(json_file_objects, path)

	def reload(self):
		''' deserialize from JSON '''

		try:
			with open(FileStorage.__file_path) as file_p:
				obj_dict = json.load(file_p)
				for item in obj_dict.values():
					class_name = item["__class__"]
					del item["__class__"]
					self.new(eval(class_name)(**item))
		except:
			pass
