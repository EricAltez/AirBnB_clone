#!/usr/bin/env python3
"""
Unitest for models/state.py

Unittest classes:
    test_state_instantiates
    test_state_save
    test_state_dict
    """

import unittest
import models
from models.state import State


class test_state_instantiates(unittest.TestCase):
    """ Unittest for testing instantiation"""

    def test_instantiation(self):
        self.assertIs(State, type(State()))

    def test_instantiation_with_kwargs(self):
        self.assertIs(State, type(State(name="California")))

    def test_save(self):
        state = State()
        state.save()
        self.assertNotEqual(state.created_at, state.updated_at)

    def test_save_updated(self):
        state = State()
        state.save()
        state.save()
        self.assertNotEqual(state.created_at, state.updated_at)

    def test_save_to_json(self):
        state = State()
        state.save()
        self.assertIs(type(state.to_dict()), dict)

    def test_none(self):
        """test for state none"""
        self.state = State()
        self.state.name = None
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(None, self.state.name)

     def test_args_unused(self):
        state1 = State(None)
        self.assertNotIn(None, state1.__dict__.values())


if __name__ == "__main__":
    unittest.main()
