import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.rectangle1 = Rectangle(10, 2)
		cls.rectangle2 = Rectangle(2, 10)
		cls.rectangle3 = Rectangle(10, 2, 0, 0, 12)
		cls.rectangle4 = Rectangle(20, 13, 5, 7)

	def test_rectangle_instance(self):
		self.assertIsInstance(self.rectangle1, Rectangle)
		self.assertIsInstance(self.rectangle2, Rectangle)
		self.assertIsInstance(self.rectangle3, Rectangle)
		self.assertIsInstance(self.rectangle4, Rectangle)

	def test_rectangle_id(self):
		self.assertEqual(self.rectangle1.id, 1)
		self.assertEqual(self.rectangle2.id, 2)
		self.assertEqual(self.rectangle3.id, 12)
		self.assertEqual(self.rectangle4.id, 3)
	
	def test_rectangle_width(self):
		self.assertEqual(self.rectangle1.width, 10)
		self.assertEqual(self.rectangle2.width, 2)
		self.assertEqual(self.rectangle3.width, 10)
		self.assertEqual(self.rectangle4.width, 20)
		with self.assertRaises(TypeError) as exc:
			Rectangle('as', 2, 0, 0, 12)
		self.assertEqual(str(exc.exception), "width must be an integer")
		with self.assertRaises(ValueError) as exc:
			Rectangle(-1, 2, 0, 0, 12)
		self.assertEqual(str(exc.exception), "width must be > 0")
		with self.assertRaises(ValueError) as exc:
			Rectangle(0, 2, 0, 0, 12)
		self.assertEqual(str(exc.exception), "width must be > 0")

	
	def test_rectangle_height(self):
		self.assertEqual(self.rectangle1.height, 2)
		self.assertEqual(self.rectangle2.height, 10)
		self.assertEqual(self.rectangle3.height, 2)
		self.assertEqual(self.rectangle4.height, 13)
		with self.assertRaises(TypeError) as exc:
			Rectangle(10, "height", 0, 0, 12)
		self.assertEqual(str(exc.exception), "height must be an integer")
		with self.assertRaises(ValueError) as exc:
			Rectangle(10, -2, 0, 0, 12)
		self.assertEqual(str(exc.exception), "height must be > 0")
		with self.assertRaises(ValueError) as exc:
			Rectangle(10, 0, 0, 0, 12)
		self.assertEqual(str(exc.exception), "height must be > 0")
	
	def test_rectangle_x(self):
		self.assertEqual(self.rectangle1.x, 0)
		self.assertEqual(self.rectangle2.x, 0)
		self.assertEqual(self.rectangle3.x, 0)
		self.assertEqual(self.rectangle4.x, 5)
		with self.assertRaises(TypeError) as exc:
			Rectangle(10, 2, "x", 0, 12)
		self.assertEqual(str(exc.exception), "x must be an integer")
		with self.assertRaises(ValueError) as exc:
			Rectangle(10, 2, -3, 0, 12)
		self.assertEqual(str(exc.exception), "x must be >= 0")
	
	def test_rectangle_y(self):
		self.assertEqual(self.rectangle1.y, 0)
		self.assertEqual(self.rectangle2.y, 0)
		self.assertEqual(self.rectangle3.y, 0)
		self.assertEqual(self.rectangle4.y, 7)
		with self.assertRaises(TypeError) as exc:
			Rectangle(10, 2, 0, "y", 12)
		self.assertEqual(str(exc.exception), "y must be an integer")
		with self.assertRaises(ValueError) as exc:
			Rectangle(10, 2, 0, -4, 12)
		self.assertEqual(str(exc.exception), "y must be >= 0")

	def test_area(self):
		self.assertEqual(self.rectangle1.area(), 20)
		self.assertEqual(self.rectangle2.area(), 20)
		self.assertEqual(self.rectangle3.area(), 20)
		self.assertEqual(self.rectangle4.area(), 260)

if __name__ == "__main__":
	unittest.main()