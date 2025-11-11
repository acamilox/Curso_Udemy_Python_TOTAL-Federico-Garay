from collections import Counter # importamos el contador
from collections import defaultdict # importamos el diccionario por defecto
from collections import namedtuple # importamos el nombre de la tupla

numeros = [8,6,9,5,4,5,5,5,8,7,4,5,4,4]
print(Counter(numeros))

serie = Counter([1,1,1,1,1,1,2,2,2,2,3,3,3,3,3,3,3,4])
print(serie.most_common(1))

# uso del defaultdict
mi_dic = defaultdict(lambda: 'nada')

mi_dic['uno'] = 'verde'
print(mi_dic['dos'])
print(mi_dic)

# uso del namedtuple
Persona = namedtuple('Persona',['nombre','altura','peso'])
ariel = Persona('Ariel',1.76,79)
print(ariel.altura)
print(ariel.peso)