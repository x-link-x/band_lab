from src.band import Band

class Manager:
    def __init__(self, name):
        self.name = name
        self.address = ""
        

    def pay_salaries(self, musicians):
        for musician in musicians:
            musician.bank += musician.salary

    def calculate_payroll(self, musicians):
        total_payroll = 0
        for musician in musicians:
            total_payroll += musician.salary
        return total_payroll
    