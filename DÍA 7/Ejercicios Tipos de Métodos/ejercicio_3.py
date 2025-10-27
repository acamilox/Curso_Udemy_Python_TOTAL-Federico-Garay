'''

Práctica Tipos de Métodos 3
Crea un método de instancia lanzar_flecha() que reste en -1 la cantidad de flechas que tiene una
instancia de Personaje, que cuenta con un atributo de instancia de tipo número,
llamado cantidad_flechas.

'''

class Personaje:
    def __init__(self, flechas_iniciales):
        self.cantidad_flechas = flechas_iniciales
        print(f"Personaje creado con {self.cantidad_flechas} flechas.")

    def lanzar_flecha(self):
        # Verifica si quedan flechas antes de restar
        if self.cantidad_flechas > 0:
            self.cantidad_flechas -= 1
            print(f"¡Flecha lanzada! Quedan {self.cantidad_flechas} flechas.")
        else:
            print("¡No quedan flechas para lanzar!")



# Creamos una instancia de Personaje con 10 flechas
mi_arquero = Personaje(10)

# Usamos el método para lanzar flechas
mi_arquero.lanzar_flecha()
mi_arquero.lanzar_flecha()

# Verificamos la cantidad restante
print(f"Flechas actuales: {mi_arquero.cantidad_flechas}")

# Lanzamos todas las flechas restantes
for _ in range(8):
    mi_arquero.lanzar_flecha()

# Intentamos lanzar una flecha más
mi_arquero.lanzar_flecha()