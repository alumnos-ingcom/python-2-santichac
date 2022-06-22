################
# Santiago Julián Chacón - @santichac
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
La sucesión de Fibonacci es una sucesión infinita donde cada elemento es
la suma de los dos anteriores. En la misma, los dos primeros términos
son 1. (En algunos lugares se toma el primer término en 0 y el segundo en 1)
Implementar una función que permita obtener el n-esimo termino de la
sucesión de Fibonacci. Siendo este número un entero positivo mayor a 2.
"""
def fibonacci(numero):
    """
    Esta función toma un número y devuelve el número
    que haya ingresado en la sucesión de fibonacci.
    Pre: numero es un número entero postivo que es el
    n-esimo número de la sucesión de fibonacci.
    Post: la función devuelve el número que haya introducido el usuario
    en la sucesión de fibonacci.
    """
    numero_a = 0
    numero_b = 1

    for x in range(numero):
        numero_c = numero_a + numero_b
        numero_a = numero_b
        numero_b = numero_c

    return numero_b

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input('Ingrese un número: '))
    print(fibonacci(numero))

if __name__ == "__main__":
    principal()
