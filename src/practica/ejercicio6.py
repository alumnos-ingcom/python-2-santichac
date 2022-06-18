################
# Santiago Julián Chacón - @santichac
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
El cifrado César o cifrado de rotación usa una encriptación de 
sustitución simple. Esto significa que cada caracter se sustituye 
por otro caracter de acuerdo con un sistema especifico. 

La codificación debe ser tal que la palabra codificada contenga 
unicamente caracteres del tipo AZaz y 0 a 9, de manera que al 
codificar las ultimas letras del abecedario se vuelva a las primeras letras.
"""

def codificar(texto, posiciones):
    conversion = 0
    codificado = ""
    diferencia = 0
    for c in texto:
        conversion = ord(c)
        if conversion >= 48 and conversion <= 57:
            while posiciones > 10:
                posiciones -= 10
            conversion += posiciones
            if conversion > 57:
                diferencia = conversion - 57
                conversion = 48
                conversion += diferencia - 1
        elif conversion >= 97 and conversion <= 122:
            while posiciones > 26:
                posiciones -= 26
            conversion += posiciones
            if conversion > 122:
                diferencia = conversion - 122
                conversion = 97
                conversion += diferencia - 1
        elif conversion >= 65 and conversion <= 90:
            while posiciones > 26:
                posiciones -= 26
            conversion += posiciones
            if conversion > 90 and conversion <= 122:
                diferencia = conversion  - 90
                conversion = 65
                conversion += diferencia - 1
        codificado += chr(conversion)
    return codificado

def decodificar(texto, posiciones):
    conversion = 0
    decodificado = ""
    for c in texto:
        conversion = ord(c)
        if conversion >= 48 and conversion <= 57:
            while posiciones > 10:
                posiciones -= 10
            conversion -= posiciones
            if conversion < 48:
                diferencia = 48 - conversion
                conversion = 57
                conversion -= diferencia - 1
        elif conversion >= 97 and conversion <= 122:
            while posiciones > 26:
                posiciones -= 26
            conversion -= posiciones
            if conversion < 97:
                diferencia = 97 - conversion
                conversion = 122
                conversion -= diferencia - 1
        elif conversion >= 65 and conversion <= 90:
            while posiciones > 26:
                posiciones -= 26
            conversion -= posiciones
            if conversion < 65:
                diferencia = 65 - conversion
                conversion = 90
                conversion -= diferencia - 1
        decodificado += chr(conversion)
    return decodificado

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    pass


if __name__ == "__main__":
    principal()
