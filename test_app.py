import unittest
from datetime import datetime
from app import today


class TestApp(unittest.TestCase):

    def test_today(self):
        self.assertEqual(today(),
                         'Current Date:{dt}'.
                         format(dt=datetime.today().strftime('%d-%m-%Y')))


if __name__ == '__main__':
    unittest.main()
