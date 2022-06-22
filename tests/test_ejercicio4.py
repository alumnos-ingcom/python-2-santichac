################
# Santiago Julián Chacón - @santichac
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from practica.ejercicio4 import fibonacci

"""
Este archivo va a probar si la función de fibonacci
del ejercicio4.py funciona.
"""

def test_fibonacci():
    """
    Este test va a probar la función de fibonacci.
    """
    numero = 10
    resultado = fibonacci(numero)
    assert isinstance(resultado, int), 'El resultado debe ser un número entero positivo.'
    assert resultado == 89, 'El resultado no es el resultado esperado.'