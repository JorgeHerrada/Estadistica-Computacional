import random
from statistics import mean
import statistics


def media(X):
    return sum(X) / len(X)


if __name__ == '__main__':

    # Get list lenght from user
    n_elements = int(input("Ingresa el largo de la lista de elementos: "))

    # list comprehension generation random elements for list within 1-20
    X = [random.randint(1,21) for i in range(n_elements)]

    # Calculate mean with custom function 
    mu1 = media(X)
    # Calculate mean with statistics library
    mu2 = statistics.mean(X)

    # Print results
    print(f'Lista de valores({n_elements}): {X}')
    print(f'Media con funcion: {mu1}')
    print(f'Media con librería: {mu2}')