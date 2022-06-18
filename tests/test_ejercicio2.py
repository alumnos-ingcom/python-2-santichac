################
# Santiago Julián Chacón - @santichac
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from practica.ejercicio2 import maximo_minimo_promedio

"""
Este test esta probando el ejercicio2.py que calcula el maximo, el minimo y el promedio
en una lista de números.
"""


def test_maximo_minimo_promedio_positivos():
    """
    Est test prueba la función maximo_minimo_promedio
    con todos números positivos.
    """
    lista = [5, 8, 1, 15, 90, 84, 114]
    resultado = maximo_minimo_promedio(lista)
    assert isinstance(resultado, tuple), 'El resultado debe ser una tupla con tres números positivos, primero el maximo, segundo el minimo y tercer el promedio entre todos.'
    assert resultado == (114, 1, 45.285714285714285), 'El resultado no es el esperado.'

def test_maximo_minimo_promedio_positivos_negativo():
    """
    Est test prueba la función maximo_minimo_promedio
    con todos números negativos.
    """
    lista = [-3, -8, -15, -7, -90, -53, -142]
    resultado = maximo_minimo_promedio(lista)
    assert isinstance(resultado, tuple), 'El resultado debe ser una tupla con tres números negativos, primero el maximo, segundo el minimo y tercer el promedio entre todos.'
    assert resultado == (-3, -142, -45.42857142857143), 'El resultado no es el esperado.'

def test_maximo_minimo_promedio_positivos():
    """
    Est test prueba la función maximo_minimo_promedio
    con todos números positivos.
    """
    lista = [-12, 7, 85, -28, 1, 176, -26]
    resultado = maximo_minimo_promedio(lista)
    assert isinstance(resultado, tuple), 'El resultado debe ser una tupla con tres números variados, primero el maximo, segundo el minimo y tercer el promedio entre todos.'
    assert resultado == (176, -28, 29.0), 'El resultado no es el esperado.'
