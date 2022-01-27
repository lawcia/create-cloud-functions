import unittest
from create_cloud_functions.main import generate
from os.path import exists


class MyTestCase(unittest.TestCase):
    def test_something(self):
        generate('hello_world')
        self.assertTrue(exists('hello_world.py'))


if __name__ == '__main__':
    unittest.main()
