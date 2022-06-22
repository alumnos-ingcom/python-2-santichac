################
# Santiago Julián Chacón - @santichac
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Implementar una función que obtenga los máximos, mínimos y promedio de 
una secuencia con números, retornando los valores como una `tuple`.

Sin utilizar lazos `for` o las funciones integradas del lenguaje 
que procesan secuencias.
"""

def maximo_minimo_promedio(lista):
    """
    Esta función recibe la cantidad de números que el usuario decida
    y obtiene el número mas grande, el mas chico y el promedio de todos los números.
    Pre: lista es una lista de números enteros, positivos o negativos.
    Post: la función devuelve una tupla con el maximo de todos, el minimo y el promedio entre todos.
    """
    maximo = lista[0]
    minimo = lista[0]
    suma = 0

    contador_maximo = len(lista) -1
    while contador_maximo >= 0:
        if lista[contador_maximo] > maximo:
            maximo = lista[contador_maximo]
        contador_maximo -=1
    
    contador_minimo = len(lista) -1
    while contador_minimo >= 0:
        if lista[contador_minimo] < minimo:
            minimo = lista[contador_minimo]
        contador_minimo -= 1
    
    contador_promedio = len(lista) -1
    while contador_promedio >= 0:
        suma += lista[contador_promedio]
        contador_promedio -= 1
    promedio = suma / len(lista)
    resultado = maximo, minimo, promedio
    return tuple(resultado)


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    lista = []
    numero = int(input('Ingrese el número de cantidad de elementos que va a ingresar: '))
    contador = 0
    resultado = 0
    while contador < numero:
        contador += 1
        resultado = int(input('Ingrese un número: '))
        lista.append(resultado)
    print(maximo_minimo_promedio(lista))

if __name__ == "__main__":
    principal()
