'''

Práctica Interrupción de Flujo
Crea un loop For a lo largo de la siguiente lista de números, imprimiendo en pantalla cada uno de
sus elementos, e interrumpe el flujo en el momento que encuentres un valor negativo:

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

No debes cambiar el orden de la lista.

'''

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for elemento in lista_numeros:
    if elemento < 0:
        break
    else:
        print(elemento)