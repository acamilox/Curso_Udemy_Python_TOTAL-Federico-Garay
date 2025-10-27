lista = ['a', 'b', 'c', 'd']

for elemento in lista:
    numero_letra = lista.index(elemento) + 1
    print(elemento)

lista = ['pablo','laura','fede','luis','julia']
for nombre in lista:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print('Nombre que no empieza con L')

numeros = [1, 2, 3, 4, 5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero

print(mi_valor)