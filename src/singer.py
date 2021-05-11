from src.musician import Musician

class Singer(Musician):
   
    def play(self):
        return f"{self.name} is singing"