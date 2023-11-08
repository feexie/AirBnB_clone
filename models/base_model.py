#!/usr/bin/python3


import uuid
from datetime import datetime
time_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:

    def __init__(self, *args, **kwargs):

        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key and key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)

    def __str__(self):
        
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        
        created_at_iso = self.created_at.isoformat()
        updated_at_iso = self.updated_at.isoformat()

        return {
            **self.__dict__,
            '__class__': self.__class__.__name__,
            'created_at': created_at_iso,
            'updated_at': updated_at_iso }
