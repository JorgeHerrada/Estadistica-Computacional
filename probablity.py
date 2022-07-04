import random

def tirar_dado(numero_de_tiros):
    # list to store the sequence of shots
    secuencia_de_tiros = []

    # itera N veces segun numero de tiros
    for _ in range(numero_de_tiros):
        
        tiro1 = random.choice([1,2,3,4,5,6])
        tiro2 = random.choice([1,2,3,4,5,6])
        # tiro = random.randint(1,7) # works same was as above
        
        # suma de ambos dados
        suma_tirada = tiro1 + tiro2 
        
        # agrega la tirada toda a la secuencia de tiros
        secuencia_de_tiros.append(suma_tirada)

    # retorna secuencia de tiros
    return secuencia_de_tiros


def main(numero_de_tiros, numero_de_intentos):
    tiros = []

    for _ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dado(numero_de_tiros)
        tiros.append(secuencia_de_tiros)
    
    tiros_con_1 = 0
    tiros_con_12 = 0

    for secuencia_de_tiros in tiros:
        # if 1 in secuencia_de_tiros:       # Probabilidad de que esté el 1
        # if 1 not in secuencia_de_tiros:     # Probabilidad de que NO esté el 1 
         if 12 in secuencia_de_tiros:     # Probabilidad de que esté el 12
            tiros_con_1 += 1
    
    probabilidad = tiros_con_1 / numero_de_intentos

    # print(f'Probabilidad de obtener por lo menos un 1 en {numero_de_tiros} tiros = {probabilidad}') # 1
    # print(f'Probabilidad de NO obtener nisiquiera un 1 en {numero_de_tiros} tiros = {probabilidad}') # NO 1
    print(f'Probabilidad de obtener por lo menos un 12 en {numero_de_tiros} tiros = {probabilidad}') # 12
    

if __name__ == '__main__':
    numero_de_tiros = int(input('Cuantos tiros del dado: '))
    numero_de_intentos = int(input('Cuantas veces correrá la simulacion: '))

    main(numero_de_tiros, numero_de_intentos)
