#!/usr/bin/python3
'''class filestorage'''
import json


class FileStorage:
    '''serialize instance to JSON'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''return the dictionary'''
        return(self.__object)

    def new(self, obj):
        '''set objects in objects with key'''
        keys = f"{obj.__class__.__name__}.{obj.id}"
        v_d = obj
        FileStorage.__objects[keys] = v_d

    def save(self):
        '''serializes objects to JSON path'''
        odic = {}
        for key, val in FileStorage.__objects.item():
            odic[key] = val.to_dict()
        with open(FileStorage.__file_path, "w+") as wf:
            json.dump(odic, wf, indent=4)

    def reload(self):
        '''deserealizes the JSON file to object'''
        pass
