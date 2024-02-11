#!/usr/bin/python3
""" this file conatins a class
that """
import json
import models


class FileStorage:
    """this class is for creating"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ description for all() methode"""
        return self.__objects

    def new(self, obj):
        """description for new() methode """
        i = str(obj.__class__.__name__) + "." + str(obj.id)
        val_dct = obj
        FileStorage.__objects[i] = val_dct

    def save(self):
        """ description for save() methode serelize"""
        dct = {}
        for key, value in FileStorage.__objects.items():
            dct[key] = value.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as f:
            json.dump(dct, f)

    def reload(self):
        """description for reload methode decerilize"""
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as f:
                FileStorage.__objects = json.load(f)
            for key, value in FileStorage.__objects.items():
                cls_name = value["__class__"]
                cls_name = models.classes[cls_name]
                FileStorage.__objects[key] = cls_name(**value)
            except FileNotFoundError:
                pass
