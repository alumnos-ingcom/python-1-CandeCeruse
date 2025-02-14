################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
2. Números positivos y negativos

Escribir una función que reciba un número e indique si el mismo es positivo,
negativo o cero utilizando sumas y restas.
"""

# Funciones del ejercicio
def signo(numero):
    """
    Esta función crea dos variable nuevas a partir del
    numero ingresado: el numero más y menos 1.
    Luego analiza esas variables comparándolas a 0 y devuelve
    si es positivo, negativo o cero.
    """
    numero_mas_1 = numero + 1
    numero_menos_1 = numero - 1
    if numero_mas_1 > 0:
        if numero_menos_1 >= 0:
            resultado = 1
        else:
            resultado = 0
    else:
        resultado = -1
    return resultado

def principal():
    """
    Al ingresar un numero la funcion signo detecta si es positivo,
    negativo, o cero. Lo hace comparando dos nuevos valores, el numero mas 1
    y el numero menos 1.
    Si el numero mas 1 es negativo entonces el numero es negativo. Sino queda
    comparar si es mayor o igual a cero, si lo es entonces es positivo, y si da
    menor que cero entonces el numero es cero.
    """
    numero_ingresado = int(input("Ingrese numero\n"))
    print("La funcion devuelve 1 si es positivo.")
    print("La funcion devuelve -1 si es negativo.")
    print("La funcion devuelve 0 si es cero.")
    print(signo(numero_ingresado))

if __name__ == "__main__":
    principal()
