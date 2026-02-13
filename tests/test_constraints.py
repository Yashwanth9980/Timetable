"""
Tests for Constraints
"""

import unittest
from config.constraints import MAX_CLASSES_PER_DAY

class TestConstraints(unittest.TestCase):
    def test_max_classes(self):
        self.assertEqual(MAX_CLASSES_PER_DAY, 6)

if __name__ == '__main__':
    unittest.main()