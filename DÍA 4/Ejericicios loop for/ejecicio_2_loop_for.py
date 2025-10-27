'''

Práctica Loop For 2
Dada la siguiente lista de números, realiza la suma de todos los números utilizando loops For
y almacena el resultado de la suma en una variable llamada suma_numeros:

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

'''

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0
for conteo in lista_numeros:
    suma_numeros = suma_numeros + conteo
    print(suma_numeros)