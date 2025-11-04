# numeros.py

from operaciones_consola import limpiar_pantalla

def generador_numeros():
    categorias = {
        "P": 0,
        "F": 0,
        "C": 0,
    }
    while True:
        letra = yield
        if letra in categorias:
            categorias[letra] += 1
            yield categorias[letra]


def decorador_mostrar_numero(funcion):
    def wrapper(numero):
        limpiar_pantalla()
        print("Su turno es:")
        numero = funcion(numero)
        print("aguarde y será atendido")
        input("Presione enter para solicitar otro turno")

    return wrapper