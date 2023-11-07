#!/usr/bin/python3


import uuid
from datetime import datetime

class BaseModel:

    def __init__(self, id=None, created_at=None, updated_at=None, name=None, my_number=None):

        self.id = id or str(uuid.uuid4())

        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

        self.name = name
        self.my_number = my_number

    def __str__(self):
        
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        updated_at = datetime.now()

    def to_dict(self):
        
        created_at_iso = self.created_at.isoformat()
        updated_at_iso = self.updated_at.isoformat()

        return {
            **self.__dict__,
            '__class__': self.__class__.__name__,
            'created_at': created_at_iso,
            'updated_at': updated_at_iso }
