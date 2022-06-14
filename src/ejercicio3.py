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
def comparacion_palabras(palabra_1, palabra_2):
    conjunto_a = set(palabra_1)
    conjunto_b = set(palabra_2)

    return tuple(conjunto_a & conjunto_b)



def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    palabra_1 = str(input('Ingrese una palabra: '))
    palabra_2 = str(input('Ingrese otra palabra: '))
    print(comparacion_palabras(palabra_1, palabra_2))


if __name__ == "__main__":
    principal()

