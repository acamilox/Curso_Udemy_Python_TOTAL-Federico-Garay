'''

Práctica Tipos de Métodos 2
Crea un método de clase revivir() que actúa sobre el atributo de clase vivo de la clase Jugador,
estableciéndolo en True cada vez que es invocado. El valor predeterminado del atributo vivo,
debe ser False.

'''

class Jugador:
    vivo = False
    def __init__(self, nombre):
        self.nombre = nombre

    @classmethod
    def revivir(cls):
        cls.vivo = True
        print(f"¡El jugador ha revivido! Estado de Jugador.vivo: {cls.vivo}")


print(f"Estado inicial de Jugador.vivo: {Jugador.vivo}")
jugador1 = Jugador('Héroe')
Jugador.revivir()