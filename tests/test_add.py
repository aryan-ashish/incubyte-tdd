import unittest


class MyTestCase(unittest.TestCase):
    def test_add_emptystring(self):
        self.assertEqual(len(""), 0)


if __name__ == '__main__':
    unittest.main()
