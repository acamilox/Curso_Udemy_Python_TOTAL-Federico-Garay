'''

Práctica Generadores 2
Crea un generador (almacenado en la variable generador) que sea capaz de devolver de manera
indefinida múltiplos de 7, iniciando desde el mismo 7, y que cada vez que sea llamado devuelva el
siguiente múltiplo (7, 14, 21, 28...).

'''

def generador():
    x = 0
    while True:
        x += 7
        yield x

# x = 0
# x = 0 + 7 = 7
# x = 7
# x = 7 + 7 = 14
# x = 14
# x = 14 + 7 = 21
# x = 21
# ...

generador_test = generador()
print(next(generador_test))
print(next(generador_test))
print(next(generador_test))
print(next(generador_test))
print(next(generador_test))