import unittest

from src.guitarist import Guitarist

class TestGuitarist(unittest.TestCase):
    
    def setUp(self):
      self.guitarist = Guitarist("Steve Marker", 100000)
    
    def test_guitarist_can_play(self):
      self.assertEqual("Steve Marker is playing guitar", self.guitarist.play())