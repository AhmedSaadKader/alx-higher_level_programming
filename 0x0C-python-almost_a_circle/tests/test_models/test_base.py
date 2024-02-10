import unittest
from models.base import Base

class TestBase(unittest.TestCase):
	def setUp(self):
		self.base1 = Base()
		self.base2 = Base()
		self.base3 = Base(5)
		self.base4 = Base()

	def test_id(self):
		self.assertEqual(self.base1.id, 1)
		self.assertEqual(self.base2.id, 2)
		self.assertEqual(self.base3.id, 5)
		self.assertEqual(self.base4.id, 3)

if __name__ == '__main__':
	unittest.main()
