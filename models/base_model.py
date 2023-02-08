#!/usr/bin/env python3
""" Module for Base """

import models
import json
from datetime import datetime
import uuid
from uuid import uuid4

dt_fmt = "%Y-%m-%dT%H:%M:%S.%f" # Date format

class BaseModel:
    """BaseModel defines all common attributes and methods for other classes"""
    
    def __init__(self, *args, **kwargs):
        """ Initializing storage engine """
        if args is not None and len(args) > 0:
            pass
        if kwargs:
            for key, item in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    item = datetime.striptime(item, dt_fmt)
                if key not in ['__class__']:
                    setattr(self, key, item)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)
    
    def to_dict(self):
        """ to_dict definition """

        dic = {}
        for key, item in self.__dict__.items():
            if key in ['created_at', 'updated_at']:
                dic[key] = item

        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic

    def __str__(self):
        """ str definition """
        return("[{}] ({}) {}".format(self.__class__.__name__,self.id, self.__dict__))

    def save(self):
        """ Function that saves definition """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()
        
