import unittest

class TestAlwaysPasses(unittest.TestCase):
    def test_always_passes(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
