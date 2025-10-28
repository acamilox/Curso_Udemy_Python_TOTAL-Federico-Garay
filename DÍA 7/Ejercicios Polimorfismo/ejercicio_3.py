'''

Práctica Polimorfismo 3

Tienes tres clases de personajes en un juego, los cuales cuentan con sus métodos de defensa
específicos.

Crea una función llamada personaje_defender(), que pueda recibir un objeto (una instancia
de las clases de tus personajes), y ejecutar su método defender() independientemente de qué
tipo de personaje se trate.

'''

class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")

def personaje_defender(personaje):
    personaje.defender()

# Instancias
mago = Mago()
arquero = Arquero()
samurai = Samurai()

# Probamos la función polimórfica con cada tipo de objeto
personaje_defender(mago)
personaje_defender(arquero)
personaje_defender(samurai)

if __name__ == '__main__':