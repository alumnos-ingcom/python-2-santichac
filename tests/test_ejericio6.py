################
# Santiago Julián Chacón - @santichac
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from practica.ejercicio6 import codificacion, decodificacion

"""
Este archivo test es para comprobar si funciona el ejercicio6.py.
"""

def test_codificacion_letras():
    """
    Este test es para comprobar que la función codificación
    funcione con palabras.
    """
    palabra_o_numero = 'milanesa'
    posicionamiento = 2
    resultado = codificacion(palabra_o_numero, posicionamiento)
    assert isinstance(resultado, str), 'El resultado debe ser una cadena de letras.'
    assert resultado == 'okncpguc', 'El resultado no es el esperado.'

def test_codificacion_numeros():
    """
    Este test es para comprobar que la función codificación
    funcione con números.
    """
    palabra_o_numero = '16'
    posicionamiento = 1
    resultado = codificacion(palabra_o_numero, posicionamiento)
    assert isinstance(resultado, str), 'El resultado debe ser una cadena de números.'
    assert resultado == '27', 'El resultado no es el esperado.'

def test_codificacion_variado():
    """
    Este test es para comprobar que la función codificación
    funcione con palabras y números a la vez.
    """
    palabra_o_numero = '14 son los pajaros'
    posicionamiento = 3
    resultado = codificacion(palabra_o_numero, posicionamiento)
    assert isinstance(resultado, str), 'El resultado debe ser una cadena de números y despues letras.'
    assert resultado == '47 vrq orv sdmdurv', 'El resultado no es el esperado.'

def test_decodificacion_letras():
    """
    Este test es para comprobar que la función decodificación
    funcione con palabras.
    """
    palabra_o_numero = 'okncpguc'
    posicionamiento = 2
    resultado = decodificacion(palabra_o_numero, posicionamiento)
    assert isinstance(resultado, str), 'El resultado debe ser una cadena de letras.'
    assert resultado == 'milanesa', 'El resultado no es el esperado.'

def test_decodificacion_numeros():
    """
    Este test es para comprobar que la función decodificación
    funcione con números.
    """
    palabra_o_numero = '27'
    posicionamiento = 1
    resultado = decodificacion(palabra_o_numero, posicionamiento)
    assert isinstance(resultado, str), 'El resultado debe ser una cadena de números.'
    assert resultado == '16', 'El resultado no es el esperado.'

def test_decodificacion_variado():
    """
    Este test es para comprobar que la función decodificación
    funcione con palabras y números a la vez.
    """
    palabra_o_numero = '47 vrq orv sdmdurv'
    posicionamiento = 3
    resultado = decodificacion(palabra_o_numero, posicionamiento)
    assert isinstance(resultado, str), 'El resultado debe ser una cadena de números y despues letras.'
    assert resultado == '14 son los pajaros', 'El resultado no es el esperado.'
