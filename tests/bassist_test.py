import unittest

from src.bassist import Bassist

class TestBassist(unittest.TestCase):
    
    def setUp(self):
      self.bassist = Bassist("Duke Erikson", 5000)
    
    def test_bassist_can_play(self):
      self.assertEqual("Duke Erikson is playing bass", self.bassist.play())