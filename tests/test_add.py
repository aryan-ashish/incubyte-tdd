import unittest
from stringcalculator.add import add


class MyTestCase(unittest.TestCase):
    def test_add_emptystring(self):
        self.assertEqual(add(""), 0)


if __name__ == '__main__':
    unittest.main()
