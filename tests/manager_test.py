import unittest

from src.manager import Manager
from src.guitarist import Guitarist
from src.bassist import Bassist
from src.singer import Singer
from src.manager import Manager

class TestManager(unittest.TestCase):
    
    def setUp(self):
      self.guitarist = Guitarist("Steve Marker", 100000)
      self.bassist = Bassist("Duke Erikson", 5000)
      self.singer = Singer("Shirley Manson", 90000)
      self.manager = Manager("Dale Caruthers")
      self.musicians = [ self.guitarist, self.bassist, self.singer]
    
    def test_manager_can_pay_salary(self):
      self.manager.pay_salaries(self.musicians)

      self.assertEqual(100000, self.guitarist.get_bank())
      self.assertEqual(5000, self.bassist.get_bank())
      self.assertEqual(90000, self.singer.get_bank())
    
    def test_band_can_calculate_payroll(self):
      self.assertEqual(195000, self.manager.calculate_payroll(self.musicians))
    
