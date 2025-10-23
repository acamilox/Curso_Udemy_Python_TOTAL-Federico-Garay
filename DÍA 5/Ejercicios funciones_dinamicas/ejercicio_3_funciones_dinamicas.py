'''

Práctica Funciones Dinámicas 3
Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista
(lista_numeros), y devuelva el resultado de dicha cuenta.

'''

lista_numeros = [1, 50, 502, 755, 34]

def cantidad_pares(lista_numeros):
    contador = 0
    for numero in lista_numeros:
        if numero%2 == 0:
            contador += 1
    return contador
