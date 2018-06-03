import unittest
from msds510 import util


class UtilTest(unittest.TestCase):

    def setUp(self):
        self.dict_x = {'a': 1, 'b': 52, 'd': 6}
        self.list_y = ['a', 'c', 'd']

    def test_float_str(self):
        self.assertEqual(util.to_int('4.4'), None)

    def test_invalid_str(self):
        self.assertEqual(util.to_int('invalid string'), None)

    def test_int_input(self):
        self.assertEqual(util.to_int('4'), 4)

    def test_valid_dict_input(self):
        self.assertEqual(util.get_value(self.dict_x, 'q'), None)
        self.assertEqual(util.get_value(self.dict_x, 'a'), 1)
        self.assertEqual(util.get_value(self.dict_x, 'b'), 52)

    def test_valid_list_input(self):
        self.assertEqual(util.get_value(self.list_y, 'd'), 2)

    def test_list_missing_key(self):
        self.assertEqual(util.get_value(self.list_y, 'b'), None)


if __name__ == '__main__':
    main()
