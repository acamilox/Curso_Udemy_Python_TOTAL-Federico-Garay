'''


Práctica Generadores 1
Crea un generador (almacenado en la variable generador) que sea capaz de devolver una secuencia
infinita de números, iniciando desde el 1, y entregando un número consecutivo superior cada vez
que sea llamada mediante next.

Pista: Utiliza un loop while para realizar este ejercicio.

'''

def generador():
    x = 0
    while True:
        x += 1
        yield x


generador_test = generador()
print(next(generador_test))
print(next(generador_test))
print(next(generador_test))