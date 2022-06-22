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
def corchetes(palabra):
    """
    """
    cantidad = 0
    corchetes_a = 0
    while corchetes_a<len(palabra):
        if palabra[corchetes_a] == '[':
            cantidad += 1
    corchetes_a += 1

    if cantidad > 0:
        print('tiene')
    else:
        print('notiene')


def corchetes_dos(palabra):
    contador = 0
    corchetes_b = 0
    while corchetes_b<len(palabra):
        if palabra[corchetes_b] == ']':
            contador += 1
    corchetes_b += 1
    
    if contador > 0:
        print('tiene')
    else:
        print('notiene')


    

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    palabra = str(input('Ingrese una cadena de caracteres con corchetes: '))
    resultado = corchetes(palabra)
    nashe = corchetes_dos(palabra) 
    print(resultado, nashe)


if __name__ == "__main__":
    principal()
