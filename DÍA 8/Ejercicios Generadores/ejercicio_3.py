'''

Práctica Generadores 3

Crea un generador que reste una a una las vidas de un personaje de videojuego, y devuelva un mensaje
cada vez que sea llamado:

"Te quedan 3 vidas"

"Te quedan 2 vidas"

"Te queda 1 vida"

"Game Over"

Almacena el generador en la variable perder_vida.

'''


def vidas():
    x = 3
    while x > 0:
        # 1. Producimos el mensaje antes de restar
        if x == 1:
            yield 'Te queda 1 vida'
        else:
            yield f'Te quedan {x} vidas'
        x -= 1

    yield 'Game Over'


perder_vida = vidas()
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))