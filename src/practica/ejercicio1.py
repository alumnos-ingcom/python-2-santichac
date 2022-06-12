################
# Santiago Julián Chacón - @santichac
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que retorne `True` cuando un número entero es par
y `False` cuando no lo sea, sin utilizar módulo. (`%`)
"""

def es_par(nro):
    """
    Esta función es para saber si un número es par o impar.
    Si el número ingresado que es nro es par el programa
    devuelve True, en el caso de que sea impar devolversa False.
    """
    numero = nro // 2
    resultado = numero + numero
    return bool(resultado == nro)

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    nro = int(input('Ingrese un número: '))
    print(es_par(nro))

if __name__ == "__main__":
    principal()
