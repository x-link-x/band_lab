import unittest

from src.band import Band
from src.guitarist import Guitarist
from src.bassist import Bassist
from src.singer import Singer
from src.manager import Manager

class TestBand(unittest.TestCase):

    def setUp(self):
        self.guitarist = Guitarist("Steve Marker", 100000)
        self.bassist = Bassist("Duke Erikson", 5000)
        self.singer = Singer("Shirley Manson", 90000)
        self.manager = Manager("Dale Caruthers")
        self.band = Band("Garbage", self.guitarist, self.bassist, self.singer, self.manager)

    def test_band_has_name(self):
        self.assertEqual("Garbage", self.band.name)
    
    def test_band_can_calculate_payroll(self):
        self.assertEqual(195000, self.band.calculate_payroll())
    
    def test_band_can_pay_salaries(self):
        old_bank = self.guitarist.get_bank()
        self.band.pay_salaries()
        new_bank = self.guitarist.get_bank()

        self.assertEqual(new_bank, old_bank + self.guitarist.get_salary())
    
    def test_band_can_play(self):
        self.assertEqual("Steve Marker is playing guitar\nDuke Erikson is playing bass\nShirley Manson is singing\n", self.band.play())
        
