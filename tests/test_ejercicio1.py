################
# Santiago Julián Chacón - @santichac
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from practica.ejercicio1 import es_par

"""
Este archivo test es para comprobar si el ejercicio1.py
funciona.
"""


def test_es_par_positivo_par():
    """
    Este test comprueba que el número introducido
    sea par.
    """
    nro = 2
    resultado = es_par(nro)
    assert isinstance(resultado, bool), 'El resultado debe ser True ya que el número es par.'
    assert resultado == True, 'El resultado no es el esperado.'

def test_es_par_positivo_impar():
    """
    Este test comprueba que el número introducido
    sea impar.
    """
    nro = 3
    resultado = es_par(nro)
    assert isinstance(resultado, bool), 'El resultado debe ser False ya que el número es impar.'
    assert resultado == False, 'El resultado no es el esperado.'

def test_es_par_negativo_par():
    """
    Este test comprueba que el número introducido
    sea par negativo.
    """
    nro = -2
    resultado = es_par(nro)
    assert isinstance(resultado, bool), 'El resultado debe ser True ya que el número es par.'
    assert resultado == True, 'El resultado no es el esperado.'

def test_es_par_negativo_impar():
    """
    Este test comprueba que el número introducido
    sea impar.
    """
    nro = -3
    resultado = es_par(nro)
    assert isinstance(resultado, bool), 'El resultado debe ser False ya que el número es impar.'
    assert resultado == False, 'El resultado no es el esperado.'