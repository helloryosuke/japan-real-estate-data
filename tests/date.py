from .context import jre
import unittest

class TestDate(unittest.TestCase):
    
    def setUp(self):

        # input and expected results upon creation of Date object from jre.common
        self.year = 2022
        self.month = 3
        self.day = 31
        self.quarter = 1
        self.date = jre.common.Date(self.year, self.month, self.day)

    def test_date_year(self):
        self.assertEqual(self.date.year, self.year)

    def test_date_month(self):
        self.assertEqual(self.date.month, self.month)

    def test_date_day(self):
        self.assertEqual(self.date.day, self.day)

    def test_date_quarter(self):
        self.assertEqual(self.date.quarter, self.quarter)


if __name__ == '__main__':
    unittest.main()
        