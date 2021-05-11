class Musician:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.bank = 0


    def get_bank(self):
        return self.bank

    def get_salary(self):
        return self.salary

    def add_money(self, amount):
        self.bank += amount

    
    