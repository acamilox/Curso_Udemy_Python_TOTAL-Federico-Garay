def suma():
    try:
        n1 = int(input('Numero 1: '))
        n2 = int(input('Numero 2: '))
        print(n1 + n2)
        print('Gracias por sumar')
        print('Hiciste todo bien')

    except ValueError:
        print('Algo no ha salido bien')
        print('Eso fue todo')

def pedir_numero():
    while True:
        try:
            numero = int(input('Dame un numero: '))
        except:
            print('Ese no es un numero')
        else:
            print(f'Ingresaste el numero {numero}')
            break

    print('Gracias')


if __name__=='__main__':
    suma()
    pedir_numero()