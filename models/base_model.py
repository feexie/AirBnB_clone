#!/usr/bin/python3
""" BaseModel class """
import uuid
import models
from datetime import datetime
time_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """ representation of BaseModel """

    def __init__(self, *args, **kwargs):
        """ init """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key and key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
        if not kwargs:
            models.storage.new(self)

    def __str__(self):
        """ __str__ repr """

        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """ save method """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ to_dict method """

        created_at_iso = self.created_at.isoformat()
        updated_at_iso = self.updated_at.isoformat()

        return {
            **self.__dict__,
            '__class__': self.__class__.__name__,
            'created_at': created_at_iso,
            'updated_at': updated_at_iso}
