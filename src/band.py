class Band:
    def __init__(self, name, guitarist, bassist, singer, manager):
        self.name = name
        self.guitarist = guitarist
        self.bassist = bassist
        self.singer = singer
        self.musicians = [self.guitarist, self.bassist, self.singer]
        self.manager = manager
        

    def play(self):
        playing_message = ""
        for musician in self.musicians:
            playing_message += f"{musician.play()}\n"
        return playing_message
    
    def calculate_payroll(self):
        return self.manager.calculate_payroll(self.musicians)


    def pay_salaries(self):
        for musician in self.musicians:
            musician.bank += musician.salary
