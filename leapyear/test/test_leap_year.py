import unittest
from leap_year import calculate_if_leap_year

class TestLeapYear(unittest.TestCase):


    def test_divide_by_4_is_leap_year(self):
        year = 2000
        self.assertTrue(calculate_if_leap_year(year))


    def test_divide_by_4_is_NOT_leap_year(self):
        year1 = 2001
        self.assertFalse(calculate_if_leap_year(year1))

    def test_divide_by_4_and_100_but_not_400_is_not_a_leap_year(self):
        year = 1700
        self.assertFalse(calculate_if_leap_year(year))

    def test_divided_by_400_is_leap_year(self):
        year = 1200
        self.assertTrue(calculate_if_leap_year(year))

    def test_divided_by_400_is_NOT_leap_year(self):
        year = 1700
        self.assertFalse(calculate_if_leap_year(year))



if __name__ == '__main__':
    unittest.main()
