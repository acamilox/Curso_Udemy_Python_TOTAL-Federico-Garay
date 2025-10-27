'''

Práctica Return 2
Crea una función llamada usd_a_eur que tome como único parámetro un valor numérico (un monto en
dólares estadounidenses), y devuelva como resultado el monto equivalente en euros. A fines de este
ejemplo, tomaremos la conversión 1 USD = 0.90 EUR.

Crea una variable llamada dolares y almacena en ella un monto cualquiera para entregárselo a tu
función y evaluar su resultado.

Pista: para realizar la conversión, la función internamente debe multiplicar este valor en dólares
por 0.90 para obtener el monto equivalente en euros.

'''

def usd_a_eur(dolares):
    return dolares * 0.90

dolares = usd_a_eur(1)
print(dolares)