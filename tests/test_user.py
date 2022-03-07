#!/usr/bin/python3
'''test user'''

import json
import unittest
from datetime import datetime
from models.user import User


class T_User(unnitest.TestCase):
    '''test user class'''

    def test_ty(self):
        '''check types'''
        clstest = User()
        self.assertEqual(type(clstest), User)
        self.assertEqual(type(clstest.id), str)
        self.assertEqual(type(clstest.created_at), datetime)
        self.assertEqual(type(clstest.updated_at), datetime)
        self.assertEqual(type(clstest.__str__()), str)
        self.assertNotEqual(len(clstest.__str__()), 0)
        self.assertEqual(type(clstest.name), str)
        self.assertEqual(str(clstest), "[User] ({}) \
        {}".format(clstest.id, clstest.__dict__))

    def test_meth(self):
        '''test method'''
        cls_test = User()
        self.assertEqual(type(cls_test.to_dict()), dict)
