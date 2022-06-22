################
# Santiago Julián Chacón - @santichac
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Implementar una función que determine si una cadena con corchetes 
está balanceada.

Es decir, si cada corchete que abre, tiene su par que cierra. 
El resultado debe ser un valor lógico indicando si esta o no balanceado.
"""
def primera(palabra):
    """
    Esta función toma el valor 0 de la lista y chequea que no sea ],
    en el caso de que sea ] devolvera False.
    Pre: palabra es una serie de corchetes introducida por el usuario.
    Post: la función devolvera True si empieza con [ y False si empieza con ].
    """
    problemas = 0
    lista =[ ]
    lista = palabra.split()
    if lista[0] == ']':
        problemas = False
    else:
        problemas = True
    return problemas

def corchetes_abre(palabra):
    """
    Esta función toma valores de la cadena de corchetes que introdujo el usuario
    y analiza si esta balanceado o no.
    Pre: palabra es una serie de corchetes introducido por el usuario.
    Post: la función devuelve el valor de la cantidad de [ que haya.
    """
    contador = 0
    validacion = 0
    for corchete_A in palabra:
        if(corchete_A == '['):
            contador += 1
            validacion += 1
    return validacion

def corchetes_cierre(palabra):
    """
    Esta función toma valores de la cadena de corchetes que introdujo el usuario
    y analiza si esta balanceado o no.
    Pre: palabra es una serie de corchetes introducido por el usuario.
    Post: la función devuelve el valor de la cantidad de ] que haya.
    """
    cantidad = 0
    validar = 0
    for corchete_B in palabra:
        if(corchete_B == ']'):
            cantidad += 1
            validar += 1
    return validar

def balanceado(validacion, validar):
    """
    Esta función toma los valores de las funciones anteriores y
    devuelve True si esta balanceado y False si no lo esta.
    Pre: validacion es el resultado de la función corchete_abre()
    validar es el resultado de la función corchetes_cierre()
    Post: si esta balanceado devolvera True y si no lo esta
    devolvera False.
    """
    balance = True
    if validacion == validar:
        balance = True
    else:
        balance = False
    return balance

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    palabra = str(input('Ingrese una cadena de caracteres con corchetes: '))
    abre = corchetes_abre(palabra)
    cierre = corchetes_cierre(palabra) 
    cualquiera = primera(palabra)
    resultado = balanceado(abre, cierre)
    print(resultado)
    print(cualquiera)

if __name__ == "__main__":
    principal()
