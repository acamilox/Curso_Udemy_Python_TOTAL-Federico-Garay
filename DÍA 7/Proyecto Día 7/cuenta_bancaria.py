# PARTE FUNCIONAL DEL CAJERO - CUENTA BANCARIA

class Persona:
    def __init__(self, nombres, apellidos):
        self.nombres = nombres
        self.apellidos = apellidos

class Cliente(Persona):
    def __init__(self, nombres, apellidos, numero_cuenta, balance):
        super().__init__(nombres, apellidos)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
            return f'''-----------------------------------------------
******  Bienvenido al Cajero Bancolombia  *****
-----------------------------------------------
Datos del Cliente
Nombres y Apellidos: {self.nombres} {self.apellidos}
Número de Cuenta: {self.numero_cuenta}
Balance: ${self.balance} '''

    # Metodo Depositar
    def depositar(self):
        monto = float(input('¿Cuánto dinero quiere agregar a su cuenta? $'))
        if monto > 0:
            self.balance += monto  # Suma al balance de la instancia
            print(f'Depósito exitoso. Nuevo balance: ${self.balance}')
        else:
            print('El monto a depositar debe ser positivo.')

    # Metodo Retirar
    def retirar(self):
        monto = float(input('¿Cuánto dinero desea retirar de su cuenta? $'))
        if monto > self.balance:
            print('Error: Fondos insuficientes.')
        elif monto <= 0:
            print('Error: El monto a retirar debe ser positivo.')
        else:
            self.balance -= monto  # Resta del balance de la instancia
            print(f'Retiro exitoso. Nuevo balance: ${self.balance}')

# CREACIÓN DEL CLIENTE
def crear_cliente():
    # Pedimos los datos
    nombres = input('Ingrese su(s) nombre(s): ').upper()
    apellidos = input('Ingrese su(s) apellido(s): ').upper()
    numero_cuenta = input('Ingrese su número de cuenta: ')
    balance = float(input('Ingrese su balance inicial: $'))
    print('')

    # Creamos y retornamos el objeto Cliente
    cliente = Cliente(nombres, apellidos, numero_cuenta, balance)
    return cliente

def inicio():
    print("--- BIENVENIDO AL SISTEMA BANCARIO ---")
    mi_cliente = crear_cliente()  # Creamos el cliente

    # Imprimimos los datos usando __str__
    print(mi_cliente)

    opcion = ''
    while opcion != '3':
        print('\n¿Qué desea hacer?')
        print('1. Depositar')
        print('2. Retirar')
        print('3. Salir')
        print('')
        opcion = input('Seleccione una opción: ')
        print('')

        if opcion == '1':
            mi_cliente.depositar()  # Llamamos al método del objeto
        elif opcion == '2':
            mi_cliente.retirar()  # Llamamos al método del objeto
        elif opcion == '3':
            print('Gracias por usar nuestros servicios.')
        else:
            print('Opción no válida.')


inicio()