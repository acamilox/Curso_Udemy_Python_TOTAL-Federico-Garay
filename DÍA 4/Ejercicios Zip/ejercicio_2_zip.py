'''

Práctica Zip 2
Crea un objeto zip formado a partir de listas, de un conjunto de marcas y productos que
tú prefieras, dentro de la variable mi_zip.

'''

marcas = ['Apple','Nike','Coca-Cola','Samsung']
productos = ['iPhone','Zapatillas Deportivas','Zero','Smartphones (Galaxy)']

mi_zip = zip(marcas,productos)

for marcas,productos in mi_zip:
    print(mi_zip)