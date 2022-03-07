#!/usr/bin/python3
'''test place'''

import json
import unittest
from datetime import datetime
from models.place import Place


class T_Place(unittest.TestCase):
    '''test place class'''

    def test_ty(self):
        '''check types'''
        clstest = Amenity()
        self.assertEqual(type(clstest), Place)
        self.assertEqual(type(clstest.id), str)
        self.assertEqual(type(clstest.created_at), datetime)
        self.assertEqual(type(clstest.updated_at), datetime)
        self.assertEqual(type(clstest.__str__()), str)
        self.assertNotEqual(len(clstest.__str__()), 0)
        self.assertEqual(type(clstest.name), str)
        self.assertEqual(str(clstest), "[Place] ({}) \
        {}".format(clstest.id, clstest.__dict__))

    def test_meth(self):
        '''test method'''
        cls_test = Place()
        self.assertEqual(type(cls_test.to_dict()), dict)
