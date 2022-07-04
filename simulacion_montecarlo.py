import random
import collections



# Definimos baraja
PALOS = ['espada','corazon','rombo','trebol']
VALORES = ['as','2','3','4','5','6','7','8','9','10','jota','reina','rey']

def crear_bajara():
    baraja = []
    for palo in PALOS:
        for valor in VALORES:
            baraja.append((palo,valor))
    
    return baraja


def obtener_mano(baraja, tamano_mano):
    # get an unreapeated set of N elements from a list
    mano = random.sample(baraja,tamano_mano)

    return mano


def main(tamano_mano,intentos):
    # Create the 
    baraja = crear_bajara()

    manos = []

    for _ in range(intentos):
        mano = obtener_mano(baraja,tamano_mano)
        manos.append(mano)

    pares = 0

    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])
        
        # Create a dictionary with {value:<occurrences>}
        counter = dict(collections.Counter(valores))
        # print(counter)

        for val in counter.values():
            if val == 2:
                pares += 1
                break
    
    probabilidad_par = pares / intentos

    print(f'La probabilidad de encontrar un par en una mano de {tamano_mano} cartas es: {probabilidad_par}')

if __name__ == '__main__':

    # get size of hand and iterations from user
    tamano_mano = int(input("De cuantas cartas sera la mano: "))
    intentos = int(input("Cuantos intentos para calcular probabilidad: "))

    # call main function
    main(tamano_mano,intentos)

    
    # barajas = crear_bajara()
    # mano = obtener_mano(barajas,5)

    
    # print(mano)
