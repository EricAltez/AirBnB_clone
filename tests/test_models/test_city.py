#!/usr/bin/python3
'''test City'''

import json
import unittest
from datetime import datetime
from models.city import City


class T_City(unittest.TestCase):
    '''test City class'''

    def test_ty(self):
        '''check types'''
        clstest = Amenity()
        self.assertEqual(type(clstest), City)
        self.assertEqual(type(clstest.id), str)
        self.assertEqual(type(clstest.created_at), datetime)
        self.assertEqual(type(clstest.updated_at), datetime)
        self.assertEqual(type(clstest.__str__()), str)
        self.assertNotEqual(len(clstest.__str__()), 0)
        self.assertEqual(type(clstest.name), str)
        self.assertEqual(str(clstest), "[City] ({}) \
        {}".format(clstest.id, clstest.__dict__))

    def test_meth(self):
        '''test method'''
        cls_test = City()
        self.assertEqual(type(cls_test.to_dict()), dict)

if __name__ == '__main__':
    unittest.main()
