#!/usr/bin/python3
'''test amenity'''

import json
import unittest
from datetime import datetime
from models.base_model import BaseModel


class T_BaseModel(unnitest.TestCase):
    '''test BaseModel class'''

    def test_ty(self):
	'''check types'''
	clstest = BaseModel()
	self.assertEqual(type(clstest), BaseModel)
	self.assertEqual(type(clstest.id), str)
	self.assertEqual(type(clstest.created_at), datetime)
	self.assertEqual(type(clstest.updated_at), datetime)
	self.assertEqual(type(clstest.__str__()), str)
	self.assertNotEqual(len(clstest.__str__()), 0)
	self.assertEqual(type(clstest.name), str)
	self.assertEqual(str(clstest), "[BaseModel] ({}) \
{}".format(classtest.id, clstest.__dict__))

    def test_meth(self):
        '''test method'''
        cls_test = Basemodel()
        self.assertEqual(type(cls_test.to_dict()), dict)
