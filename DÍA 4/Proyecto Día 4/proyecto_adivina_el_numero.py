import random

def adivina_el_numero():
    """
    Función principal para el juego de adivinar el número.
    """
    print("========================================")
    print(" ¡Bienvenido a Adivina el Número! ")
    print("========================================")
    print("Estoy pensando en un número entre 1 y 100.")

    # Se genera un número aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)

    intentos = 8
    adivinado = False

    while not adivinado:
        try:
            # Se solicita al usuario que ingrese un número
            intento_usuario = int(input("\n¿Cuál crees que es el número?: "))
            intentos += 1

            # Se compara el número del usuario con el número secreto
            if intento_usuario < numero_secreto:
                print("¡Demasiado bajo! Intenta con un número más grande. ⬆️")
            elif intento_usuario > numero_secreto:
                print("¡Demasiado alto! Intenta con un número más pequeño. ⬇️")
            else:
                adivinado = True
                print("\n***************************************************")
                print(f"🎉 ¡Felicidades! ¡Adivinaste el número en {intentos} intentos! 🎉")
                print(f"El número secreto era el {numero_secreto}.")
                print("***************************************************")

        except ValueError:
            # Manejo de error si el usuario no ingresa un número
            print("❌ Error: Por favor, introduce solo números válidos.")


# Iniciar el juego
if __name__ == "__main__":
    adivina_el_numero()