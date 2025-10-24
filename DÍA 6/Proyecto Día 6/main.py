import os
import shutil
from pathlib import Path

# --- Configuración Inicial ---

# Obtenemos la ruta 'home' del usuario y creamos la ruta a la carpeta 'Recetas'
# Path.home() es multiplataforma (funciona en Windows, Mac y Linux)
ruta_base = Path("Recetas")

# --- Funciones Auxiliares (Utilidades) ---

def limpiar_pantalla():
    """Limpia la pantalla de la consola, compatible con Windows, Mac y Linux."""
    # 'nt' es para Windows, 'posix' para Mac/Linux
    os.system('cls' if os.name == 'nt' else 'clear')


def volver_al_menu():
    """Pausa la ejecución hasta que el usuario presione Enter."""
    input("\nPresiona Enter para volver al menú principal...")


def contar_recetas(ruta: Path) -> int:
    """
    Cuenta recursivamente todos los archivos .txt dentro de la ruta base.

    Args:
        ruta: El objeto Path de la carpeta 'Recetas'.

    Returns:
        El número total de recetas (archivos .txt).
    """
    # .rglob('*.txt') busca recursivamente (en todas las subcarpetas)
    # archivos que terminen en .txt
    conteo = len(list(ruta.rglob("*.txt")))
    return conteo


def validar_opcion(min_val: int, max_val: int) -> int | None:
    """
    Solicita al usuario un número entre min_val y max_val y lo valida.

    Args:
        min_val: El número mínimo aceptable.
        max_val: El número máximo aceptable.

    Returns:
        El número entero validado.
    """
    while True:
        opcion_str = input(f"Elige una opción (del {min_val} al {max_val}): ")
        if not opcion_str.isdigit():
            print("Error: Debes ingresar un número.")
            continue

        opcion_int = int(opcion_str)
        if min_val <= opcion_int <= max_val:
            return opcion_int
        else:
            print(f"Error: Opción fuera de rango (debe ser entre {min_val} y {max_val}).")


# --- Funciones de Lógica Principal (Elegir/Mostrar) ---

def elegir_categoria(ruta: Path) -> Path | None:
    """
    Muestra las categorías (carpetas) disponibles y permite al usuario elegir una.

    Args:
        ruta: El objeto Path de la carpeta 'Recetas'.

    Returns:
        Un objeto Path a la categoría elegida, o None si no hay categorías.
    """
    print("Categorías disponibles:")

    # .iterdir() lista el contenido, filtramos solo por directorios
    categorias = [d for d in ruta.iterdir() if d.is_dir()]

    if not categorias:
        print("No se encontraron categorías.")
        return None

    for i, categoria in enumerate(categorias):
        print(f"[{i + 1}] - {categoria.name}")

    # Validamos la elección del usuario
    opcion_valida = validar_opcion(1, len(categorias))

    # Devolvemos el objeto Path de la categoría seleccionada
    return categorias[opcion_valida - 1]


def elegir_receta(ruta_categoria: Path) -> Path | None:
    """
    Muestra las recetas (archivos .txt) en una categoría y permite al usuario elegir una.

    Args:
        ruta_categoria: El objeto Path de la carpeta de la categoría seleccionada.

    Returns:
        Un objeto Path a la receta elegida, o None si no hay recetas.
    """
    print(f"Recetas en '{ruta_categoria.name}':")

    # .glob('*.txt') busca archivos .txt solo en este nivel
    recetas = [f for f in ruta_categoria.glob("*.txt") if f.is_file()]

    if not recetas:
        print("No se encontraron recetas en esta categoría.")
        return None

    for i, receta in enumerate(recetas):
        # .stem nos da el nombre del archivo sin la extensión .txt
        print(f"[{i + 1}] - {receta.stem}")

    opcion_valida = validar_opcion(1, len(recetas))

    return recetas[opcion_valida - 1]


# --- Funciones del Menú (Opciones 1-6) ---

def mostrar_bienvenida(ruta: Path):
    """Muestra el mensaje de bienvenida, la ruta y el conteo de recetas."""
    print("¡Bienvenido al Administrador de Recetas! 🍳")
    print("============================================")
    print(f"Las recetas se encuentran en: {ruta}")
    conteo = contar_recetas(ruta)
    print(f"Actualmente tienes un total de: {conteo} recetas.")
    print("============================================")


def mostrar_menu():
    """Imprime las opciones del menú principal."""
    print("\nMenú Principal:")
    print("[1] - Leer receta")
    print("[2] - Crear receta nueva")
    print("[3] - Crear categoría nueva")
    print("[4] - Eliminar receta")
    print("[5] - Eliminar categoría")
    print("[6] - Salir del programa")


def opcion_1_leer_receta(ruta_base: Path):
    """Lógica para la Opción 1: Leer Receta."""
    limpiar_pantalla()
    print("== Leer Receta ==")

    categoria_elegida = elegir_categoria(ruta_base)
    if not categoria_elegida:
        return  # Vuelve al menú si no hay categorías

    receta_elegida = elegir_receta(categoria_elegida)
    if not receta_elegida:
        return  # Vuelve al menú si no hay recetas

    limpiar_pantalla()
    # .read_text() es un método de Path que abre, lee y cierra el archivo
    print(f"--- Mostrando: {receta_elegida.name} ---")
    print(receta_elegida.read_text(encoding="utf-8"))
    print("---------------------------------------")


def opcion_2_crear_receta(ruta_base: Path):
    """Lógica para la Opción 2: Crear Receta."""
    limpiar_pantalla()
    print("== Crear Receta ==")

    categoria_elegida = elegir_categoria(ruta_base)
    if not categoria_elegida:
        return

    # Pedir nombre de la nueva receta
    nombre_receta = input("\nIngresa el nombre de la nueva receta: ")
    # Construimos el path final
    path_nueva_receta = categoria_elegida / (nombre_receta + ".txt")

    if path_nueva_receta.exists():
        print(f"Error: La receta '{nombre_receta}.txt' ya existe en esta categoría.")
        return

    # Pedir contenido
    contenido_receta = input("Escribe el contenido de la receta (presiona Enter al finalizar):\n")

    # .write_text() crea y escribe en el archivo
    path_nueva_receta.write_text(contenido_receta, encoding="utf-8")

    print(f"¡Receta '{nombre_receta}.txt' creada exitosamente en '{categoria_elegida.name}'!")


def opcion_3_crear_categoria(ruta_base: Path):
    """Lógica para la Opción 3: Crear Categoría."""
    limpiar_pantalla()
    print("== Crear Categoría ==")

    nombre_categoria = input("Ingresa el nombre de la nueva categoría: ")
    path_nueva_categoria = ruta_base / nombre_categoria

    if path_nueva_categoria.exists():
        print(f"Error: La categoría '{nombre_categoria}' ya existe.")
        return

    # .mkdir() crea el directorio
    path_nueva_categoria.mkdir()
    print(f"¡Categoría '{nombre_categoria}' creada exitosamente!")


def opcion_4_eliminar_receta(ruta_base: Path):
    """Lógica para la Opción 4: Eliminar Receta."""
    limpiar_pantalla()
    print("== Eliminar Receta ==")

    categoria_elegida = elegir_categoria(ruta_base)
    if not categoria_elegida:
        return

    receta_elegida = elegir_receta(categoria_elegida)
    if not receta_elegida:
        return

    # Confirmación de seguridad
    confirmar = input(f"¿Estás seguro de que deseas eliminar '{receta_elegida.name}'? (s/n): ").lower()

    if confirmar == 's':
        # .unlink() elimina el archivo
        receta_elegida.unlink()
        print(f"Receta '{receta_elegida.name}' eliminada.")
    else:
        print("Eliminación cancelada.")


def opcion_5_eliminar_categoria(ruta_base: Path):
    """Lógica para la Opción 5: Eliminar Categoría."""
    limpiar_pantalla()
    print("== Eliminar Categoría ==")

    categoria_elegida = elegir_categoria(ruta_base)
    if not categoria_elegida:
        return

    # Confirmación de seguridad
    confirmar = input(f"¡ADVERTENCIA! Esto eliminará la carpeta '{categoria_elegida.name}' "
                      "y TODAS las recetas que contiene.\n"
                      "¿Estás seguro? (s/n): ").lower()

    if confirmar == 's':
        # shutil.rmtree() elimina un directorio y todo su contenido
        # Es más robusto que .rmdir() que requiere que esté vacío
        shutil.rmtree(categoria_elegida)
        print(f"Categoría '{categoria_elegida.name}' y todo su contenido han sido eliminados.")
    else:
        print("Eliminación cancelada.")


# --- Bucle Principal (main) ---

def main():
    """Función principal que ejecuta el bucle del programa."""

    # Verificamos si la carpeta base 'Recetas' existe
    if not ruta_base.exists() or not ruta_base.is_dir():
        print(f"Error: No se encontró el directorio de recetas en '{ruta_base}'")
        print("Por favor, crea la carpeta 'Recetas' en tu directorio Home.")
        print("Ejemplo de estructura:")
        print("Recetas/")
        print("  ├── Carnes/")
        print("  │   ├── Lomo Saltado.txt")
        print("  │   └── Pollo al Curry.txt")
        print("  └── Ensaladas/")
        print("      └── Ensalada César.txt")
        return  # Termina el script si la carpeta no existe

    opcion_elegida = 0

    # El bucle while principal se repite hasta que la opción sea 6
    while opcion_elegida != 6:
        limpiar_pantalla()
        mostrar_bienvenida(ruta_base)
        mostrar_menu()

        opcion_elegida = validar_opcion(1, 6)

        # Ejecutamos la función correspondiente
        if opcion_elegida == 1:
            opcion_1_leer_receta(ruta_base)
        elif opcion_elegida == 2:
            opcion_2_crear_receta(ruta_base)
        elif opcion_elegida == 3:
            opcion_3_crear_categoria(ruta_base)
        elif opcion_elegida == 4:
            opcion_4_eliminar_receta(ruta_base)
        elif opcion_elegida == 5:
            opcion_5_eliminar_categoria(ruta_base)

        # Si la opción no es 6, pausamos antes de repetir el bucle
        if opcion_elegida != 6:
            volver_al_menu()

    # Mensaje de despedida al salir del bucle
    limpiar_pantalla()
    print("¡Gracias por usar el Administrador de Recetas! ¡Hasta pronto! 👋")

# --- Punto de Entrada del Script ---
if __name__ == "__main__":
    main()