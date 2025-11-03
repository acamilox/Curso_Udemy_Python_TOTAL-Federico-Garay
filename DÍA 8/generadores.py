def mi_funcion():
    lista = []
    for x in range(1, 5):
        lista.append(x * 10)
    return lista

# uso del generador
def mi_generador():
    for x in range(1, 5):
        yield x * 10


print(mi_funcion())
print(mi_generador())
g = mi_generador()

print(next(g)) # usamos el next para el generador
print(next(g)) # usamos el next para el generador