################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
9. Factores Primos

Escribir una función que retorne una tuple con
factores primos de un numero entero positivo.
"""

# Funciones del ejercicio
def factores_primos(numero):
    """
    Primero crea una lista vacia de primos y establece el divisor en 2.
    Entonces, mientras que el numero sea mayor que 1,  se pregunta si
    el resto de la divison de numero por divisor es cero. Si lo es numero
    se convierte en el cociente entero de numero/divisor. Luego se guarda
    el divisor en la lista de primos.
    """
    lista_primos = []
    divisor = 2
    while numero > 1:
        if numero % divisor == 0:
            numero = numero // divisor
            lista_primos.append(divisor)
        else:
            divisor+=1
    tupla_primos = tuple(lista_primos)
    return tupla_primos

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input("Ingrese numero entero: "))
    print(f"Factores primos: {factores_primos(numero)}")

if __name__ == "__main__":
    principal()
