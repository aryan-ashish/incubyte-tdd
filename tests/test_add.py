import unittest
from stringcalculator.add import add


class MyTestCase(unittest.TestCase):
    def test_add_emptystring(self):
        self.assertEqual(add(""), 0)

    def test_add_single_arg(self):
        self.assertEqual(add("99"), 99)

    def test_add_two_args(self):
        self.assertEqual(add("1,2"), 3)


if __name__ == '__main__':
    unittest.main()
