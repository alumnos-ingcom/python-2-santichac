################
# Santiago Julián Chacón - @santichac
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from practica.ejercicio3 import palabras_similares

"""
Este test prueba el ejercicio3.py que calcula el grado de
superposición entre dos palabras.
"""


def test_palabras_similares_iguales():
    """
    Este test prueba la función palabras_similares
    con dos palabras iguales.
    """
    palabra_1 = 'hola'
    palabra_2 = 'hola'
    resultado = palabras_similares(palabra_1, palabra_2)
    assert isinstance(resultado, int), 'El resultado debe ser 4.'
    assert resultado == 4, 'El resultado no es el esperado.'

def test_palabras_similares():
    """
    Este test prueba la función palabras_similares
    con dos palabras similares.
    """
    palabra_1 = 'maseta'
    palabra_2 = 'jirafa'
    resultado = palabras_similares(palabra_1, palabra_2)
    assert isinstance(resultado, int), 'El resultado debe ser 1.'
    assert resultado == 1, 'El resultado no es el esperado.'

def test_palabras_similares_distintas():
    """
    Este test prueba la función palabras_similares
    con dos palabras completamente distintas.
    """
    palabra_1 = 'perro'
    palabra_2 = 'musica'
    resultado = palabras_similares(palabra_1, palabra_2)
    assert isinstance(resultado, int), 'El resultado debe ser 0.'
    assert resultado == 0, 'El resultado no es el esperado.'
    