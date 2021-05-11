import unittest

from src.musician import Musician

class TestMusician(unittest.TestCase):
    
    def setUp(self):
        self.musician = Musician("Steve Marker", 100000)
    
    def test_musician_can_get_salary(self):
      self.assertEqual(100000, self.musician.get_salary())
    
    def test_musician_can_get_bank(self):
      self.assertEqual(0, self.musician.get_bank())
    
    def test_musician_can_add_money(self):
      self.musician.add_money(10)
      self.assertEqual(10, self.musician.get_bank())