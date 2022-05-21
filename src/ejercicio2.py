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
    numero_original = numero
    numero_mas_1 = numero + 1
    numero_menos_1 = numero - 1
    if numero_mas_1 > 0:
        if numero_menos_1 >= 0:
            print("Es positivo")
        else:
            print("Es cero")
    else:
        print("Es negativo")

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
    signo(numero_ingresado)
    pass

if __name__ == "__main__":
    principal()

"""
Fin del ejercicio
"""