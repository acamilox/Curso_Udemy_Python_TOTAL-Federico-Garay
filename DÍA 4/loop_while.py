monedas = 5

while monedas > 0:
    print(f'Tengo {monedas} monedas')
    monedas = monedas - 1
else:
    print('No tengo más dinero')


respuesta = 's'
while respuesta == 's':
    respuesta = input('¿Quieres continuar? (s/n): ')
else:
    print('Gracias por participar')


nombre = input('Tu nombre: ')

for letra in nombre:
    if letra == 'r:':
        continue
    print(letra)