import random
import collections
from typing import Tuple
from numpy import sort



# Definimos baraja
PALOS = ['espada','corazon','rombo','trebol']
VALORES = [i for i in range(1,14) ]
JUGADAS_GANADORAS = ["par","dos pares","tercia","escalera","color","full house","poker","escalera de color","escalera imperial"]

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


def par(manos, intentos, diccionario):
    pares = 0

    # Iterate for each hand in list of hands
    for mano in manos:
        # list of values
        valores = []
        # Iterate for each card on hand
        for carta in mano:
            # add value no mather the suit of the card
            valores.append(carta[1])
        
        # Create a dictionary with this format: {value:<occurrences>}
        counter = dict(collections.Counter(valores))
        # print(counter)

        # for each value in dictionary
        for val in counter.values():
            # if its a pair increase pair counter and finish iteration
            if val == 2:
                pares += 1
                break
    
    # Calculate the posibility based on the number of pairs found in all the hands that we got
    return pares / intentos


def dos_pares(manos, intentos, diccionario):
    # total of two pairs found on all hands
    dobles_pares = 0

    # Iterate for each hand in list of hands
    for mano in manos:
        # number of pairs found in each hand
        pares = 0

        # list of values
        valores = []
        
        # GET CARDS VALUES 
        # Iterate for each card on hand
        for carta in mano:
            # add value no mather the suit of the card
            valores.append(carta[1])
        
        # Create a dictionary with this format: {value:<occurrences>}
        counter = dict(collections.Counter(valores))
        # print(counter)

        # for each value in dictionary
        for val in counter.values():
            # if its a pair increase pair counter and finish iteration
            if val == 2:
                pares += 1
        
        if pares == 2:
            dobles_pares += 1
    
    # Calculate the posibility based on the number of pairs found in all the hands that we got
    return dobles_pares / intentos


def tercia(manos, intentos, diccionario):
    tercias = 0

    # Iterate for each hand in list of hands
    for mano in manos:
        # list of values
        valores = []
        # Iterate for each card on hand
        for carta in mano:
            # add value no mather the suit of the card
            valores.append(carta[1])
        
        # Create a dictionary with this format: {value:<occurrences>}
        counter = dict(collections.Counter(valores))
        # print(counter)

        # for each value in dictionary
        for val in counter.values():
            # if its a pair increase pair counter and finish iteration
            if val == 3:
                tercias += 1
                break
    
    # Calculate the posibility based on the number of pairs found in all the hands that we got
    return tercias / intentos


def escalera(manos,intentos,diccionario):
    escaleras = 0

    # Iterate for each hand in list of hands
    for mano in manos:
        # list of values
        valores = []

        # Iterate for each card on hand to get its values
        for carta in mano:
            # add value no mather the suit of the card
            valores.append(carta[1])
        
        # sort values
        valores = sort(valores)

        # if there is an (AS)1 as FIRST and a (king)13 as LAST
        # change the value of as to 14 and sort values again
        # so that, we can have the straight 10 to AS (10-14)
        if 1 == valores[0] and 13 == valores[-1]:
            valores[0] = 14
            valores = sort(valores)

        # create aux hand with an straight from first to last value of hand
        aux_hand = [ i for i in range(valores[0],valores[-1] + 1)]

        # counter to keep track of each match on values with the aux_hand
        contador = 0

        # if the values are actually a straight, they will have the same lenght
        if len(valores) == len(aux_hand):

            # Iterate on each element to confirm they all match
            for i in range(0,len(valores)):
                if valores[i] == aux_hand[i]:
                    contador += 1
            
            # if all of them do, we have found an effective straight
            if contador == 5:
                escaleras += 1

                # print to confirm
                # print(f'Escalera encontrada: {valores} + {aux_hand}')
                
    
    # Calculate the posibility based on the number of straights found in all the hands that we got
    return escaleras / intentos


def color(manos,intentos,diccionario):
    # number of flushes found
    colores = 0

    # iterate for each hand in hands' list
    for mano in manos:
        # list of values
        valores = []

        # iterate for each card on hand to get it's suit
        for carta in mano:
            valores.append(carta[0])

        # counter to 
        contador = 0

        for i in range(0,5):
            if valores[0] == valores[i]:
                contador += 1
        
        if contador == 5:
            colores += 1

            # print(f"Se ha encontrado un COLOR: {mano}")
    
    return colores / intentos


def full_house(manos, intentos, diccionario):
    full_houses = 0

    # Iterate for each hand in list of hands
    for mano in manos:
        # list of values
        valores = []

        tercia = False
        par = False

        # Iterate for each card on hand
        for carta in mano:
            # add value no mather the suit of the card
            valores.append(carta[1])
        
        # Create a dictionary with this format: {value:<occurrences>}
        counter = dict(collections.Counter(valores))
        # print(counter)

        # for each value in dictionary
        for val in counter.values():
            # if its a pair increase pair counter and finish iteration
            if val == 3:
                tercia = True
            elif val == 2:
                par = True
        
        if tercia and par:
            full_houses += 1
            
    
    # Calculate the posibility based on the number of pairs found in all the hands that we got
    return full_houses / intentos






def main(tamano_mano,intentos):
    # Create deck of cards
    baraja = crear_bajara()

    # list that will contain N hands based on "intentos" variable
    manos = []

    # iterate to get N hands and add them to "manos"
    for _ in range(intentos):
        # get a random hand with N elements
        mano = obtener_mano(baraja,tamano_mano)
        # add hand to list of hands
        manos.append(mano)

    
    # Can posibly work on the future, not sure where to use it yet
    diccionario = { JUGADAS_GANADORAS[i] : 0 for i in range(len(JUGADAS_GANADORAS))}
    # print(diccionario)


    probabilidad_par = par(manos, intentos ,diccionario)
    probabilidad_doble_par = dos_pares(manos, intentos ,diccionario)
    probabilidad_tercia = tercia(manos, intentos ,diccionario)
    probabilidad_escalera = escalera(manos, intentos ,diccionario)
    probabilidad_color = color(manos, intentos ,diccionario)
    probabilidad_full_house = full_house(manos, intentos ,diccionario)

    print(f'La probabilidad de encontrar un par en una mano de {tamano_mano} cartas es: {probabilidad_par}')
    print(f'La probabilidad de encontrar dos pares en una mano de {tamano_mano} cartas es: {probabilidad_doble_par}')
    print(f'La probabilidad de encontrar una tercia en una mano de {tamano_mano} cartas es: {probabilidad_tercia}')
    print(f'La probabilidad de encontrar una escalera en una mano de {tamano_mano} cartas es: {probabilidad_escalera}')
    print(f'La probabilidad de encontrar un color en una mano de {tamano_mano} cartas es: {probabilidad_color}')
    print(f'La probabilidad de encontrar un full house en una mano de {tamano_mano} cartas es: {probabilidad_full_house}')

if __name__ == '__main__':

    # get size of hand from user
    # tamano_mano = int(input("De cuantas cartas sera la mano: "))

    # comment upper line and change this value to keep fix size of hand
    tamano_mano = 5 

    # get number of hands to simulate
    # intentos = int(input("Cuantos intentos para calcular probabilidad: "))
    
    # comment upper line and change this value to keep fix size of hand
    intentos = 10000

    # call main function
    main(tamano_mano,intentos)

    
