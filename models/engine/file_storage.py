#!/usr/bin/python3
"""Defines a FileStorage class"""
import json


class FileStorage:
    """
    class FileStorage
    Representing an abstracted storage test_engine.
    
    It serializes instances to a JSON file and deserializes 
    JSON file to instances
    Attributes:
        __file_path: string - path to the JSON file
        __objects: dictionary - empty but will store all objects.
    """
    
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
    
    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        object_dict = {}
        for obj in self.__objects:
            object_dict[obj] = self.__objects[obj].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(object_dict, file)
    
    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file does not
        exist, no exception should be raised)
        """
        
        try:
            with open(self.__file_path) as file:
                serialized_content = json.load(file)
                for item in serialized_content.values():
                    class_name = item['__class__']
                    self.new(eval(class_name + "(**" + str(item) + ")"))
        except FileNotFoundError:
            pass