class Padre:
    def hablar(self):
        print('Hola')

class Madre:
    def reir(self):
        print('ja ja ja')

    def hablar(self):
        print('que tal?')

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()
mi_nieto.hablar() # el método hablar lo heredó de hijo que hereda de padre y madre
# mi_nieto.reir() # el método reir lo heredó de hijo que hereda de padre y madre
print(Nieto.__mro__)