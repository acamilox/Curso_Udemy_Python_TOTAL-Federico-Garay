from random import randint, choice, shuffle

# from random import *

aleatorio = randint(1, 50)
print(aleatorio)

colores = ['azul', 'rojo', 'verde', 'amarillo']
aleatorio = choice(colores)

numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)