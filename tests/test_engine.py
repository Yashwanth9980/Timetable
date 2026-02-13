"""
Tests for Engine
"""

import unittest
from engine.timetable_engine import TimetableEngine

class TestEngine(unittest.TestCase):
    def test_generate(self):
        engine = TimetableEngine()
        result = engine.generate_timetable({})
        self.assertIsInstance(result, dict)

if __name__ == '__main__':
    unittest.main()