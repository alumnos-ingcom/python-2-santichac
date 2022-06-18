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

def codificacion(palabra_o_numero, posicionamiento):
    """
    Esta función codifica hacia delante cada caracter de acuerdo al número que quiera
    desplazarlo el usuario. ejemplo: abc, si se desplaza una vez,va a ser bcd
    Pre: palabra_o_numero es una o varias palabras en mayuscula o minuscula, números o una conbinación.
    posicionamiento es el valor de dezplazamiento para la encriptación de la palabra.
    Post: esta función devolvera la codificación de la palabra, las palabras, los números o
    de la combinación de ambos, según lo que quiera desplazarlo el usuario. Esto depende
    de que número introduzca el usuario.
    """
    conversion = 0
    codificacion = ''
    dif = 0
    for n in palabra_o_numero:
        conversion = ord(n)
        if conversion >= 48 and conversion <= 57:
            while posicionamiento > 10:
                posicionamiento -= 10
            conversion += posicionamiento
            if conversion > 57:
                dif = conversion - 57
                conversion = 48
                conversion += dif - 1
        elif conversion >= 97 and conversion <= 122:
            while posicionamiento > 26:
                posicionamiento -= 26
            conversion += posicionamiento
            if conversion > 122:
                dif = conversion - 122
                conversion = 97
                conversion += dif - 1
        elif conversion >= 65 and conversion <= 90:
            while posicionamiento > 26:
                posicionamiento -= 26
            conversion += posicionamiento
            if conversion > 90 and conversion <= 122:
                dif = conversion  - 90
                conversion = 65
                conversion += dif - 1
        codificacion += chr(conversion)
    return codificacion

def decodificacion(palabra_o_numero_b, posicionamiento):
    """
    Esta función decodifica la palabra que se haya codificado anteriormente. 
    Ejemplo: abc, codificada en 1 es bcd y decodificada es abc
    Pre: palabra_o_numero es una o varias palabras en mayuscula o minuscula, números o una combinación.
    posicionamiento es el valor de dezplazamiento para la encriptación de la palabra.
    Post: esta función devolvera la codificación de la palabra, las palabras, los números o
    de la combinación de ambos, hacia atras y la cantidad de el valor de desplazamiento de lo que
    haya introducido el usuario.
    """
    conversion = 0
    decodificacion = ''
    for n in palabra_o_numero_b:
        conversion = ord(n)
        if conversion >= 48 and conversion <= 57:
            while posicionamiento > 10:
                posicionamiento -= 10
            conversion -= posicionamiento
            if conversion < 48:
                dif = 48 - conversion
                conversion = 57
                conversion -= dif - 1
        elif conversion >= 97 and conversion <= 122:
            while posicionamiento > 26:
                posicionamiento -= 26
            conversion -= posicionamiento
            if conversion < 97:
                dif = 97 - conversion
                conversion = 122
                conversion -= dif - 1
        elif conversion >= 65 and conversion <= 90:
            while posicionamiento > 26:
                posicionamiento -= 26
            conversion -= posicionamiento
            if conversion < 65:
                dif = 65 - conversion
                conversion = 90
                conversion -= dif - 1
        decodificacion += chr(conversion)
    return decodificacion

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    
    palabra_o_numero = str(input('Ingrese una palabra: '))
    posicionamiento = int(input('Ingrese el valor de desplazamiento: '))
    resultado_a = codificacion(palabra_o_numero, posicionamiento)
    palabra_o_numero_b = resultado_a
    resultado_b = decodificacion(palabra_o_numero_b, posicionamiento)
    print(f'La palabra "{palabra_o_numero}" codificada es "{resultado_a}" y la decodificación de "{resultado_a}" es "{resultado_b}".')


if __name__ == "__main__":
    principal()
