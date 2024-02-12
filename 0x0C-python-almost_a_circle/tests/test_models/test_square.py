import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    @classmethod	
    def setUpClass(cls):
        cls.square1 = Square(2)
