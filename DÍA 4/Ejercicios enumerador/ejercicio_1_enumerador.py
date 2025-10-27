'''

Práctica Enumerador 1
Imprime en pantalla frases como la siguiente:

'{nombre} se encuentra en el índice {indice}'

Donde nombre debe ser cada uno de los nombres de la lista a continuación, y el índice, obtenido
mediante enumerate().

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano",
"Melisa"]

Puedes modificar la línea print() otorgada como ejemplo, pero las frases entregadas deberán ser
iguales.

Tip: utiliza loops!

'''

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for nombre, indice in enumerate(lista_nombres):
    print(f'{indice} se encuentra en el índice {nombre}')