import unittest
import main


class TestMasterMind(unittest.TestCase):

    def test_input(self):
        self.assertTrue(main.validate_input(5), True)
        self.assertFalse(main.validate_input(-1), False)
        self.assertFalse(main.validate_input(8), False)
        self.assertFalse(main.validate_input(1111), False)
        self.assertFalse(main.validate_input("five"), False)


if __name__ == '__main__':
    unittest.main()
