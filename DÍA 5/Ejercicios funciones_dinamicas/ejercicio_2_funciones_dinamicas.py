'''

Práctica Funciones Dinámicas 2
Crea una función (suma_menores) que sume los números de una lista
(almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000, y
devuelva el resultado de dicha suma.

'''

def suma_menores(lista_numeros):
    suma_total = 0
    for numero in lista_numeros:
        if 0 < numero < 1000:
            suma_total += numero
    return suma_total

lista_numeros = [1, 50, 500, 5000, 750]
result = suma_menores(lista_numeros)
print(result)