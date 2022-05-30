################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que indique con True si un numero indicado es Primo.
"""
# Funciones del ejercicio
def es_primo(numero):
    """
    Las sgtes condiciones son para los casos especiales de 2 y 3
    Y para definir de que forma usar el divisor eficientemente.
    """
    divisor = 1
    if numero == 2 or numero == 3:
        divisor = 2
    elif numero == 1:
        respuesta_booleana = False
        resultado = 'no es primo'
    else:
        divisor=numero//2

    #aca esta el bucle
    while divisor>1:
        if numero % divisor == 0 and numero != divisor:
            resultado='no es primo'
            respuesta_booleana = False
            break
        else:
            resultado='es primo'
            respuesta_booleana = True
        divisor = divisor - 1
    return resultado, respuesta_booleana

def principal():
    """
    Este es un programa que indica si un
    número ingresado es primo o no. Un número
    primo es un número entero mayor que 1 que
    tiene únicamente dos divisores positivos
    distintos: él mismo y el 1. Por ejemplo; 7
    """
    numero = int(input('Ingrese numero: '))
    resultado, respuesta_booleana = es_primo(numero)
    print(f"{numero}: {respuesta_booleana}, {resultado}")

if __name__ == "__main__":
    principal()
 