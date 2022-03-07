#!/usr/bin/python3
'''test amenity'''

import json
import unittest
from datetime import datetime
from models.base_model import BaseModel


class T_BaseModel(unittest.TestCase):
    '''test BaseModel class'''

    def test_ty(self):
        '''check types'''
        cls_test = BaseModel()
        self.assertEqual(type(cls_test), BaseModel)
        self.assertEqual(type(cls_test.id), str)
        self.assertEqual(type(cls_test.created_at), datetime)
        self.assertEqual(type(cls_test.updated_at), datetime)
        self.assertEqual(type(cls_test.__str__()), str)
        self.assertNotEqual(len(cls_test.__str__()), 0)
        self.assertEqual(type(cls_test.name), str)
        self.assertEqual(str(cls_test), "[BaseModel] ({}) \
        {}".format(cls_test.id, cls_test.__dict__))

    def test_meth(self):
        '''test method'''
        cls_test = Basemodel()
        self.assertEqual(type(cls_test.to_dict()), dict)
