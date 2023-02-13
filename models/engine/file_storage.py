#!/usr/bin/env python3

from models import base_model, user, city, review, amenity, state, place
from os.path import exists
from json import load, dump, dumps

BaseModel = base_model.BaseModel
User = user.User
City = city.City
Review = review.Review
Amenity = amenity.Amenity
State = state.State
Place = place.Place

name_class = ["BaseModel", "User", "City", "Review", "Amenity", "State", "Place"]

class FileStorage:
    """ Intializing file storage """
    __file_path = "file.json"
    __object = {}

    def all(self):
        """ Returns the dictionary object """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        class_name = obj.__class__.__name__
        id = obj.id
        class_id = class_name + "." + id
        FileStorage.__objects[class_id] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path) """
        dict_to_json = {}
        for key, value in FileStorage.__objects.items():
            dict_to_json[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding='utf-8') as fil:
            dump(dict_to_json, fil)

    def reload(self):
        """ Deserializes the JSON file to __objects (only if the JSON file (_file_path) exists; otherwise, do nothing. If the file doesn't exist, no exception should be raised """
        dict_obj = {}
        FileStorage.__objects = {}
        if (exists(FileStorage.__file_path)):
            with open(FileStorage.__file_path, "r") as fil:
                dict_obj = load(fil)
                for key, value in dic_obj.items():
                    class_nam = key.split(".")[0]
                    if class_nam in name_class:
                        FileStorage.__objects[key] = eval(class_nam)(**value)
                    else:
                        pass



