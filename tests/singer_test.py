import unittest

from src.singer import Singer

class TestSinger(unittest.TestCase):
    
    def setUp(self):
      self.singer = Singer("Shirley Manson", 90000)
    
    def test_singer_can_play(self):
      self.assertEqual("Shirley Manson is singing", self.singer.play())