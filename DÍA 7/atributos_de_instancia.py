class Pajaro:
    # Definimos los atributos de una clase (Constructor)
    alas =  True
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

mi_pajaro = Pajaro('negro', 'Tucan')

print(mi_pajaro.especie)
print(f'Mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}')
print(Pajaro.alas)
print(mi_pajaro.alas)