import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    def setUp(self):
        self.base1 = Base()
        self.base2 = Base()
        self.base3 = Base(15)
        self.base4 = Base()
    
    def tearDown(self):
        del self.base1
        del self.base2
        del self.base3
        del self.base4

    def test_base_id(self):
        self.assertEqual(self.base1.id, 4)
        self.assertEqual(self.base2.id, 5)
        self.assertEqual(self.base3.id, 15)
        self.assertEqual(self.base4.id, 6)

    def test_base_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, '[{"id": 10, "width": 10, "height": 7, "x": 2, "y": 8}]')

    def test_base_from_json_string(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4}, 
            {'id': 25, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'id': 89, 'width': 10, 'height': 4}, {'id': 25, 'width': 1, 'height': 7}])

if __name__ == '__main__':
    unittest.main()
