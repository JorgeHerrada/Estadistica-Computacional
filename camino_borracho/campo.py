class Campo:

    def __init__(self):
        # diccionario de coordenadas de los borrachos
        self.coordenadas_borrachos = {}
    

    # Añade borracho al diccionario y su coordenada actual
    def add_borracho(self, borracho, coordenada):
        self.coordenadas_borrachos[borracho] = coordenada

    # mueve al borracho un paso
    def mover_borracho(self, borracho):
        # obtiene direccion random para mover borracho y guarda en los deltas
        delta_x, delta_y = borracho.walk()

        # obtiene la coordenada actual
        coordenada_actual = self.coordenadas_borrachos[borracho]

        # define una nueva coordenada al modificar la actual
        # con el moviento random del borracho guardado en los deltas
        nueva_coordenada = coordenada_actual.mover(delta_x,delta_y)

        # fija la nueva coordenada actual del borracho en el diccionario
        self.coordenadas_borrachos[borracho] = nueva_coordenada

    # retorna coordenada (objeto de clase Coordenada) actual del borracho en cuestion
    def get_coordenada(self, borracho):
        return self.coordenadas_borrachos[borracho]
    