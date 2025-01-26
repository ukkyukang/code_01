import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
print("sys_path : ", sys.path)
from code_01.package_02 import src_02

print("module_test",src_02.function_01())

class TestModule1(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(src_02.function_01(), "hi src02")

if __name__ == '__main__':
    unittest.main()