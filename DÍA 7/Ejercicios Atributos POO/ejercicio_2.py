'''

Práctica Atributos 2

Crea una clase llamada Cubo, y asígnale el atributo de clase:

caras = 6

y el atributo de instancia:

color

Crea una instancia cubo_rojo, de dicho color.

'''

class Cubo:
    caras = 6
    def __init__(self, color):
        self.color = color


cubo_rojo = Cubo('rojo')
print(cubo_rojo.caras, cubo_rojo.color)
