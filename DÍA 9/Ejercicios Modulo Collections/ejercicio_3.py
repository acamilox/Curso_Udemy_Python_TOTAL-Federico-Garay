'''

Práctica Módulo Collections 3

Una cola doblemente terminada o deque (del inglés double ended queue) es una estructura de datos
lineal que permite insertar y eliminar elementos por ambos extremos.

Investiga más al respecto en cualquier sitio de documentación, y a continuación implementa
una deque a partir del módulo collections. Los elementos iniciales de la lista se brindan a
continuación.

["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]

La lista debe tener la capacidad de incorporar elementos por la izquierda, y recibir el nombre
lista_ciudades.

'''

from collections import deque

ciudades_iniciales = ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]

# 1. Crear la deque a partir de la lista inicial
lista_ciudades = deque(ciudades_iniciales)

# Mostrar la deque inicial
print(f"Deque inicial: {lista_ciudades}")
print(f"Tipo: {type(lista_ciudades)}")

# 2. Incorporar un elemento por la izquierda (usando appendleft)
nueva_ciudad = "Lisboa"

# Eliminar "Lisboa" para volver al estado inicial
lista_ciudades.popleft()
print(f"Deque después de popleft(): {lista_ciudades}")

# Output: deque(['Londres', 'Berlin', 'París', 'Madrid', 'Roma', 'Moscú'])

