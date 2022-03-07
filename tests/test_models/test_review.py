#!/usr/bin/python3
'''test review'''

import json
import unittest
from datetime import datetime
from models.review import Review


class T_Review(unittest.TestCase):
    '''test review class'''

    def test_ty(self):
        '''check types'''
        clstest = review()
        self.assertEqual(type(clstest), Review)
        self.assertEqual(type(clstest.id), str)
        self.assertEqual(type(clstest.created_at), datetime)
        self.assertEqual(type(clstest.updated_at), datetime)
        self.assertEqual(type(clstest.__str__()), str)
        self.assertNotEqual(len(clstest.__str__()), 0)
        self.assertEqual(type(clstest.name), str)
        self.assertEqual(str(clstest), "[Review] ({}) \
        {}".format(clstest.id, clstest.__dict__))

    def test_meth(self):
        '''test method'''
        cls_test = Review()
        self.assertEqual(type(cls_test.to_dict()), dict)
