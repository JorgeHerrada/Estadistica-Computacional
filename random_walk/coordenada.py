class Coordenada:

    def __init__(self, x , y):
        self.x = x
        self.y = y
    
    # suma coordenada actual  + nueva coordenada 
    # obteniendo nueva coordenada y retornandola
    def mover(self, delta_x, delta_y):
        return Coordenada(self.x + delta_x, self.y + delta_y)

    # calcula y retorna la distancia entre dos coordenadas
    def distancia(self, otra_coordenada):
        delta_x = self.x - otra_coordenada.x
        delta_y = self.y - otra_coordenada.y

        return (delta_x**2 + delta_y**2)**0.5
