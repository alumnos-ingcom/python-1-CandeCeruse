################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
10. Palíndromo

Escribir una función que indique con True si una palabra o
frase ingresada se trata de un palindromo. Palíndromo, es si se lee
igual de derecha a izquierda que de izquierda a derecha.
"""
# Funciones del ejercicio
def es_palindromo(palabra):
    """
    Esta funcion toma la frase o palabra ingresada y le limpia los espacios.
    Luego compara el primer y ultimo caracter yendo hacia el centro de la
    cadena sucesivamente. Si los caracteres estan espejados en el centro,
    devuelve True, dado que es un palindromo.
    """
    texto = palabra.replace(" ","")
    posicion_inicio = -len(texto)
    posicion_fin = len(texto)-1
    while posicion_fin >= 0 :
        if texto[posicion_inicio] == texto[posicion_fin]:
            posicion_inicio += 1
            posicion_fin -= 1
            palindromo = True
        else:
            palindromo = False
            break
    return palindromo

def principal():
    """
    Esta función toma una frase o palabra y la envia a la funcion
    es_palindromo. Luego muestra el resultado.
    """
    palabra = input("Ingrese palabra: ")
    print(es_palindromo(palabra))

if __name__ == "__main__":
    principal()
