def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return 1
    
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)


def fibonacci_dinamico(n, memo = {}):
    # base scenarios
    if n == 0 or n == 1:
        return 1
    
    try:
        # el valor de fibonacci de n ya fue calculado?
        return memo[n]
    except KeyError:
        # si no, calculamos de manera regular
        resultado = fibonacci_dinamico(n - 1, memo) + fibonacci_dinamico(n - 2, memo)
        # guardamos el resultado para posteriores accesos
        memo[n] = resultado
        # imprime todo el diccionario, solo para fines ilustrativos
        print(memo)
        # retornamos resultado
        return resultado



if __name__ == '__main__':

    n = int(input("Numero de fibonacci a calcular: "))
    
    # respuesta = fibonacci_recursivo(n)
    respuesta = fibonacci_dinamico(n)
    
    print(respuesta)
