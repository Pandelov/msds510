import unittest
from msds510 import util


class TestCase(unittest.TestCase):

    def setUp(self):
        self.name_alias = 'Henry Jonathan "Hank" Pym'
        self.url = 'http://marvel.wikia.com/Henry_Pym_(Earth-616)'
        self.appearances = '1269'
        self.current = 'YES'
        self.death1 = 'YES'
        self.death2 = ''
        self.death3 = ''
        self.death4 = ''
        self.death5 = ''
        self.full_reserve_avengers_intro = 'Sep-63'
        self.gender = 'MALE'
        self.honorary = 'Full'
        self.notes = 'Merged with Ultron in Rage of Ultron Vol. 1. A funeral was held. \n'
        self.probationary_introl = ''
        self.return1 = 'NO'
        self.return2 = ''
        self.return3 = ''
        self.return4 = ''
        self.return5 = ''
        self.year = '1963'
        self.years_since_joining = '52'

    def test_int_input(self):
        check_int = to_int(self.appearances)
        self.assertTrue(type(check_int) == int)

    def test_float_str(self):
        self.assertEqual(util.to_int('4.4'), None)

    def test_invalid_str(self):
        self.assertEqual(util.to_int('invalid string'), None)

    def test_valid_dict_input(self):
        self.assertEqual(util.get_value(self.x, 'q'), None)
        self.assertEqual(util.get_value(self.x, 'a'), 1)
        self.assertEqual(util.get_value(self.x, 'b'), 52)

    def test_valid_list_input(self):
        self.assertEqual(util.get_value(self.y, 'd'), 2)

    def test_list_missing_key(self):
        self.assertEqual(util.get_value(self.y, 'b'), None)

    def test_get_date(self):
        self.assertTrue(util(get_date('May-63')) == '1963-05-01')


if __name__ == '__main__':
    unittest.main()
