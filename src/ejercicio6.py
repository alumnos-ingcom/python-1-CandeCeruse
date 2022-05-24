################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
6. Ordenar 3 valores

Escribir una función que a partir de tres variables
de tipo entero retorne una tupla con dichos valores
ordenados de menor a mayor. Y Viceversa
"""
# Funciones del ejercicio
def ordenar_mayor_a_menor(uno, dos, tres):
    """
    Esta funcion compara, a través de un for, los componentes
    de la cadena. Y los reordena de mayor a menor.
    """
    cadena = [uno, dos, tres]
    for i in range(2):
        if cadena[i] < cadena[i+1]:
            posicion_a = cadena[i]
            posicion_b = cadena[i+1]
            cadena[i] = posicion_b
            cadena[i+1] = posicion_a
    #Para ordenar los primeros digitos si se da una condicion
    #de 3,2,1
    for i in range(2):
        if cadena[i] < cadena[i+1]:
            posicion_a = cadena[i]
            posicion_b = cadena[i+1]
            cadena[i] = posicion_b
            cadena[i+1] = posicion_a
    return cadena

def ordenar_menor_a_mayor(uno, dos, tres):
    """
    Esta funcion compara, a través de un for, los componentes
    de la cadena. Y los reordena de menor a mayor.
    """
    cadena = [uno, dos, tres]
    for i in range(2):
        if cadena[i] > cadena[i+1]:
            posicion_a = cadena[i]
            posicion_b = cadena[i+1]
            cadena[i] = posicion_b
            cadena[i+1] = posicion_a
    #Para ordenar los primeros digitos si se da una condicion
    #de 3,2,1
    for i in range(2):
        if cadena[i] > cadena[i+1]:
            posicion_a = cadena[i]
            posicion_b = cadena[i+1]
            cadena[i] = posicion_b
            cadena[i+1] = posicion_a
    return cadena

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    num_a = int(input('Ingrese numero a: '))
    num_b = int(input('Ingrese numero b: '))
    num_c = int(input('Ingrese numero c: '))

    menor_a_mayor = ordenar_menor_a_mayor(num_a, num_b, num_c)
    mayor_a_menor = ordenar_mayor_a_menor(num_a, num_b, num_c)

    print(f"\nMenor a mayor: {menor_a_mayor}")
    print(f"\nMayor a menor: {mayor_a_menor}")

if __name__ == "__main__":
    principal()
