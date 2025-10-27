class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal ha nacido')

class Pajaro(Animal):
    pass

# print(Pajaro.__bases__) # Me indica de quién hereda la clase Pajaro
# print(Animal.__subclasses__())


piolin = Pajaro(2,'amarillo')
print(piolin.color)