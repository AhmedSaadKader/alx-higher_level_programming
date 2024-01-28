#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_string(self):
        self.assertEqual(max_integer("adf"), "f")

    def test_list_string(self):
        self.assertEqual(max_integer(["ahmed", "arafat", "yalla"]), "yalla")

    def test_list_integers(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_list_integers_different_order(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_list_float_different_order(self):
        self.assertEqual(max_integer([2.0, 4.0, 3.0, 1.0]), 4.0)
