import JSON
import os


class fileStorage:

	def __init__(self, *args, **kwargs):
		self.__file_path = "file.json"
		self.__objects = {}

	def all(self):
		return (self.__objects)

	def new(self, obj):
		className = self.obj.__class__.__name__
		obj_key = className + '.' + obj.id
		__objects['key'] = obj_key

	def save(self):
		with open(self.__file_path, 'w') as path:
			json.dumps(self.__objects, path)

	def reload(self):

		with open(self.__file_path, 'r') as path:
            date = json.load(f)
