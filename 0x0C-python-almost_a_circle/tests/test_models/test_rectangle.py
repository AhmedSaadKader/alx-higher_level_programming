import unittest
import io
import sys
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.rectangle1 = Rectangle(3, 2)
		cls.rectangle2 = Rectangle(1, 4)
		cls.rectangle3 = Rectangle(2, 2, 0, 0, 12)
		cls.rectangle4 = Rectangle(3, 1, 5, 7)
		cls.r_update = Rectangle(10, 10, 10, 10)
		cls.r_upd_kwargs = Rectangle(5, 5, 5, 5)
	
	def test_rectangle_arguments(self):
		pass

	def test_rectangle_instance(self):
		self.assertIsInstance(self.rectangle1, Rectangle)
		self.assertIsInstance(self.rectangle2, Rectangle)
		self.assertIsInstance(self.rectangle3, Rectangle)
		self.assertIsInstance(self.rectangle4, Rectangle)

	def test_rectangle_id(self):
		self.assertEqual(self.rectangle1.id, 8)
		self.assertEqual(self.rectangle2.id, 9)
		self.assertEqual(self.rectangle3.id, 12)
		self.assertEqual(self.rectangle4.id, 10)
	
	def test_rectangle_width(self):
		self.assertEqual(self.rectangle1.width, 3)
		self.assertEqual(self.rectangle2.width, 1)
		self.assertEqual(self.rectangle3.width, 2)
		self.assertEqual(self.rectangle4.width, 3)
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
		self.assertEqual(self.rectangle2.height, 4)
		self.assertEqual(self.rectangle3.height, 2)
		self.assertEqual(self.rectangle4.height, 1)
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

	def test_rectangle_area(self):
		self.assertEqual(self.rectangle1.area(), 6)
		self.assertEqual(self.rectangle2.area(), 4)
		self.assertEqual(self.rectangle3.area(), 4)
		self.assertEqual(self.rectangle4.area(), 3)

	def capture_stdout(self, rectangle, method):
		captured_output = io.StringIO()
		sys.stdout = captured_output
		if method == "display":
			rectangle.display()
		elif method == "print":
			print(rectangle)
		sys.stdout = sys.__stdout__
		output = captured_output.getvalue()
		captured_output.close()
		return output

	def test_rectangle_display_without_x_y(self):
		self.assertEqual(self.capture_stdout(self.rectangle1, "display"), "###\n###\n")
		self.assertEqual(self.capture_stdout(self.rectangle2, "display"), "#\n#\n#\n#\n")
		self.assertEqual(self.capture_stdout(self.rectangle3, "display"), "##\n##\n")

	def test_rectangle_str_method(self):
		self.assertEqual(self.capture_stdout(self.rectangle1, "print"), "[Rectangle] (8) 0/0 - 3/2\n")
		self.assertEqual(self.capture_stdout(self.rectangle2, "print"), "[Rectangle] (9) 0/0 - 1/4\n")
		self.assertEqual(self.capture_stdout(self.rectangle3, "print"), "[Rectangle] (12) 0/0 - 2/2\n")
		self.assertEqual(self.capture_stdout(self.rectangle4, "print"), "[Rectangle] (10) 5/7 - 3/1\n")

	def test_rectangle_display_with_x_y(self):
		self.assertEqual(self.capture_stdout(self.rectangle4, "display"), "\n\n\n\n\n\n\n     ###\n")
		self.assertEqual(self.capture_stdout(Rectangle(3, 2, 2, 2), "display"), "\n\n  ###\n  ###\n")
	
	def capture_update(self, rectangle, *args):
		rectangle.update(*args)
		return self.capture_stdout(rectangle, "print")

	def test_rectangle_update_args(self):
		print(self.r_update)
		self.assertEqual(self.capture_stdout(self.r_update, "print"), "[Rectangle] (11) 10/10 - 10/10\n")
		self.assertEqual(self.capture_update(self.r_update.update(89)), "[Rectangle] (89) 10/10 - 10/10\n") 
		self.assertEqual(self.capture_update(self.r_update.update(89, 2)), "[Rectangle] (89) 10/10 - 2/10\n") 
		self.assertEqual(self.capture_update(self.r_update.update(89, 2, 3)), "[Rectangle] (89) 10/10 - 2/3\n") 
		self.assertEqual(self.capture_update(self.r_update.update(89, 2, 3, 4)), "[Rectangle] (89) 4/10 - 2/3\n") 
		self.assertEqual(self.capture_update(self.r_update.update(89, 2, 3, 4, 5)), "[Rectangle] (89) 4/5 - 2/3\n") 

	def test_rectangle_update_kwargs(self):
		print(self.r_update)
		self.assertEqual(self.capture_stdout(self.r_upd_kwargs, "print"), "[Rectangle] (12) 5/5 - 5/5\n")
		self.assertEqual(self.capture_update(self.r_upd_kwargs.update(id=89)), "[Rectangle] (89) 5/5 - 5/5\n") 
		self.assertEqual(self.capture_update(self.r_upd_kwargs.update(id=89, width=2)), "[Rectangle] (89) 5/5 - 2/5\n") 
		self.assertEqual(self.capture_update(self.r_upd_kwargs.update(id=89, width=2, height=3)), "[Rectangle] (89) 5/5 - 2/3\n") 
		self.assertEqual(self.capture_update(self.r_upd_kwargs.update(id=89, width=2, height=3, x=4)), "[Rectangle] (89) 4/5 - 2/3\n") 
		self.assertEqual(self.capture_update(self.r_upd_kwargs.update(id=89, width=2, height=3, x=4, y=6)), "[Rectangle] (89) 4/6 - 2/3\n") 
		self.assertEqual(self.capture_update(self.r_upd_kwargs.update(89, 3, width=2)), "[Rectangle] (89) 4/6 - 3/3\n") 


if __name__ == "__main__":
	unittest.main()