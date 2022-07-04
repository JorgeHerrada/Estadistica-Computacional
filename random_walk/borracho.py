import random


class Borracho:
    def __init__(self, name):
        self.name = name

class BorrachoTradicional(Borracho):
    def __init__(self, name):
        super().__init__(name)
    
    def walk(self):
        # Obtiene una direccion random entre 4 direcciones de plano cartesiano
        return random.choice([(0,1),(1,0),(-1,0),(0,-1)])
