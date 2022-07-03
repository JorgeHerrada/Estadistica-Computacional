from borracho import BorrachoTradicional
from coordenada import Coordenada
from campo import Campo

from bokeh.plotting import figure, show

x_para_graficar = []
y_para_graficar = []

# GRAFICACION
def graficar(x,y):
    grafica = figure(title='Camino aleatorio', x_axis_label = 'pasos',y_axis_label = 'distancia recorrida')
    grafica.line(x,y, legend_label = 'distancia media')

    show(grafica)


# Simula la caminata 
def caminata(campo, borracho, pasos):
    # marca inicio en coordenada actual del borracho
    inicio = campo.get_coordenada(borracho)

    # itera al Nsimo paso del respectivo intento
    for _ in range(pasos):

        # obtiene coordenadas y las pasa a lista para despues graficar las listas de coordenadas
        x_para_graficar.append(campo.get_coordenada(borracho).x)
        y_para_graficar.append(campo.get_coordenada(borracho).y)
        
        # Mueve al borracho un paso
        campo.mover_borracho(borracho)

    # terminada la caminata de n pasos, calcula y retorna la distancia entre inicio y final
    return inicio.distancia(campo.get_coordenada(borracho))

    # Simulamos la caminata, mandando el numero de pasos por caminata, 
    # numero de intentos por cada caminata y tipo de borracho
    # Retorna una lista con las distancias finales al terminar cada intento de caminata
def simular_caminata(pasos, numero_intentos, tipo_borracho):
    
    # Creamos borracho
    borracho = tipo_borracho(name='Jorge')

    # creamos coordenada de origen 
    origen = Coordenada(0,0)
    
    # creamos arreglo de distancias que almacena 
    # la distancia del punto final al origen en cada caminata de n pasos
    distancias = []

    # iteramos 1 vez por cada intento realizando una caminata
    # elemento "_" se usa cuando no se va a hacer uso del iterador
    for _ in range(numero_intentos):
        # creamos el campo donde caminará el borracho
        campo = Campo()

        # añadimos borracho  y punto de origen 
        campo.add_borracho(borracho, origen)

        # simulamos caminata para este intento de n pasos con el borracho en cuestion
        simulacion_caminata = caminata(campo, borracho, pasos)

        # guardamos distancias redondeadas
        distancias.append(round(simulacion_caminata, 1))
    
    return distancias




def main(distancias_caminata,numero_intentos, tipo_borracho):

    # para graficacion
    # distancias_media_por_caminata = []

    # Iteramos por cada tipo de caminatas y pasos es el numero de pasos de dicha caminata
    for pasos in distancias_caminata:

        # Simulamos la caminata, mandando el numero de pasos por caminata, 
        # numero de intentos por cada caminata y tipo de borracho
        distancias = simular_caminata(pasos, numero_intentos, tipo_borracho)
        # Retorna una lista con las distancias finales al terminar cada intento de caminata


        # Estadisticas:
        distancia_media = round(sum(distancias) / len(distancias),5)
        distancia_max = max(distancias)
        distancia_min = min(distancias)
        
        # graficacion
        # distancias_media_por_caminata.append(distancia_media)
        
        # Impresion de estadisticas
        print(f'{tipo_borracho.__name__}  caminata aleatoria de {pasos} pasos ')
        print(f'Media = {distancia_media}  '  )
        print(f'Maxima = {distancia_max}  '  )
        print(f'Min = {distancia_min}  '  )
    
    
    # Grafica camino del borracho
    graficar(x_para_graficar,y_para_graficar)

    




if __name__ == '__main__':

    # Lista con numero de pasos por cada caminata (4 tipos de caminatas de diferente numero de pasos)
    distancias_caminata = [10,100,1000,10000]
    # numero de veces a repetir cada tipo de caminata
    numero_intentos = 100

    # main
    main(distancias_caminata, numero_intentos, BorrachoTradicional)


