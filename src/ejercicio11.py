################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que indique con True si un número entero
es multiplo de otro, utilizando sumas y restas.
"""
# Funciones del ejercicio
def es_multiplo(numero, multiplo):
    """
    Esta funcion compara el multiplo y el numero mientras
    que el primero sea mayor o igual que el segundo. Luego,
    si no son iguales, resta el numero al multiplo
    sucesivamente hasta que sean iguales o que el resultado
    sea menor que el numero.
    """
    resultado = False
    while multiplo >= numero:
        if multiplo != numero:
            resultado = False
            multiplo = multiplo - numero
        else:
            resultado = True
            break
    return resultado

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    Ingresa las variables y ejecuta la funcion, luego muestra el resultado.
    """
    multiplo = int(input("Ingrese multiplo: "))
    numero = int(input("Ingrese numero: "))
    print(es_multiplo(numero, multiplo))

if __name__ == "__main__":
    principal()
