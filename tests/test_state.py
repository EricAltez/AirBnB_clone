#!/usr/bin/python3
'''test state'''

import json
import unittest
from datetime import datetime
from models.state import State


class T_State(unnitest.TestCase):
    '''test ameity class'''

    def test_ty(self):
	'''check types'''
	clstest = Amenity()
	self.assertEqual(type(clstest), State)
	self.assertEqual(type(clstest.id), str)
	self.assertEqual(type(clstest.created_at), datetime)
	self.assertEqual(type(clstest.updated_at), datetime)
	self.assertEqual(type(clstest.__str__()), str)
	self.assertNotEqual(len(clstest.__str__()), 0)
	self.assertEqual(type(clstest.name), str)
	self.assertEqual(str(clstest), "[State] ({}) \
{}".format(clstest.id, clstest.__dict__))

    def test_meth(self):
        '''test method'''
        cls_test = State()
        self.assertEqual(type(cls_test.to_dict()), dict)
