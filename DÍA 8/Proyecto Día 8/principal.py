from operaciones_consola import limpiar_pantalla
from numeros import decorador_mostrar_numero, generador_numeros

numerador_farmacia = generador_numeros()

opciones_numeros = {
    "P": "Perfumería",
    "F": "Farmacia",
    "C": "Cosméticos",
}


def generar_numero(letra):
    next(numerador_farmacia)
    numero = numerador_farmacia.send(letra)
    return f"{letra}-{numero}"


@decorador_mostrar_numero
def mostrar_numero(numero):
    print(numero)


def mostrar_menu():
    print("Tomar número")
    for opcion in opciones_numeros:
        print(f"[{opcion}]: {opciones_numeros[opcion]}")


def preguntar_opcion():
    opcion = ""
    while opcion not in opciones_numeros:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input("Ingresa una opción: ").upper()
        if opcion in opciones_numeros:
            mostrar_numero(generar_numero(opcion))
        opcion = ""


preguntar_opcion()