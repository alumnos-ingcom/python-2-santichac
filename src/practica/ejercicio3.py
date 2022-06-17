################
# Santiago Julián Chacón - @santichac
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Desarrollar una función que indique el grado de superposición entre dos listas.
Siendo 0 sin superposición y uno para cada elemento superpuesto.
```python
['H', 'o', 'l', 'a', ' ', 'M', 'u', 'n', 'd', 'o']
```
y 
```python
['H', 'o', 'l', 'a']
```
Tienen una superposición de cuatro elementos.
"""
def palabras_similares(palabra_1, palabra_2):
    """
    Esta función toma dos palabras, las compara y si
    tienen las mismas letras en los mismos lugares
    devolvera el grado de superposición, o sea la cantidad
    de letras iguales en el mismo lugar entre las dos palabras.
    Pre: palabra_1 y palabra_2 son dos palabras o frases con letras,
    mayusculas o minusculas y con o sin espacion.
    Post: la función devolvera un número que se usara en la función principal.
    """
    contador_1 = len(palabra_1)
    contador_2 = len(palabra_2)
    elem_palabra_1 = 0
    elem_palabra_2 = 0
    comparacion = 0
    if contador_1 > contador_2:
        while contador_2 > 0:
            if palabra_1[elem_palabra_1] == palabra_2[elem_palabra_2]:
                comparacion += 1
            elem_palabra_1 += 1
            elem_palabra_2 += 1
            contador_2 -= 1
    else:
        while contador_1 > 0:
            if palabra_1[elem_palabra_1] == palabra_2[elem_palabra_2]:
                comparacion += 1
            elem_palabra_1 += 1
            elem_palabra_2 += 1
            contador_1 -= 1
    return comparacion



def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    palabra_1 = str(input('Ingrese una palabra: '))
    palabra_2 = str(input('Ingrese otra palabra: '))
    resultado = palabras_similares(palabra_1, palabra_2)
    print(resultado)

if __name__ == "__main__":
    principal()
