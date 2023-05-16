import unittest
from main import calc


class TestCalcMethods(unittest.TestCase):
    def test_calc(self):
        predict = calc(10, 20)
        self.assertEqual(predict, 30)


if __name__ == '__main__':
    unittest.main()
