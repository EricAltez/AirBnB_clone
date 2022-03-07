#!/usr/bin/python3
'''test amenity'''

import json
import unittest
from datetime import datetime
from models.amenity import Amenity


class T_Amenity(unittest.TestCase):
    '''test ameity class'''

    def test_ty(self):
        '''check types'''
        clstest = Amenity()
        self.assertEqual(type(clstest), Amenity)
        self.assertEqual(type(clstest.id), str)
        self.assertEqual(type(clstest.created_at), datetime)
        self.assertEqual(type(clstest.updated_at), datetime)
        self.assertEqual(type(clstest.__str__()), str)
        self.assertNotEqual(len(clstest.__str__()), 0)
        self.assertEqual(type(clstest.name), str)
        self.assertEqual(str(clstest), "[Amenity] ({}) \
        {}".format(clstest.id, clstest.__dict__))

    def test_meth(self):
        '''test method'''
        cls_test = Amenity()
        self.assertEqual(type(cls_test.to_dict()), dict)

if __name__ == '__main__':
    unittest.main()
