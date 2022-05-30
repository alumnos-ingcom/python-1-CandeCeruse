################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
1. Conversión de temperaturas

Se quiere transformar temperaturas en grados fahrenheit a
grados centígrados y viceversa.

Escribir las funciones para convertir la temperatura en
grados centigrados en fahrenheit como un número decimal,
utilice esta formula para calcular los grados centígrados
y retorne el resultado obtenido. Y viceversa.
"""

#FUNCIONES:

def convertir_a_fahrenheit(valor_a_convertir):
    """
    Esta función convierte de grados centigrados
    a grados fahrenheit.
    """
    convertido_a_fahrenheit = float(((valor_a_convertir * 9) / 5) + 32 )
    return convertido_a_fahrenheit

def convertir_a_centigrados(valor_a_convertir):
    """
    Esta funcion convierte de grados fahrenheit
    a grados centigrados nuevamente.
    """
    convertido_a_centigrados = float(((valor_a_convertir - 32) * 5) / 9)
    return convertido_a_centigrados

def principal():
    """
    Este programa toma el input de grados centigrados,
    los envia a la función convertir_a_fahrenheit y la
    salida en fahrenheit es convertida a grados centigrados
    de nuevo. Al final muestra los resultados.
    """

    centigrados = int(input("Ingrese grados centigrados\n"))

    fahrenheit = convertir_a_fahrenheit(centigrados)
    nuevos_centigrados = convertir_a_centigrados(fahrenheit)

    print(f"{centigrados: .2f} grados centigrados son {fahrenheit: .2f} grados fahrenheit")
    print(f"{fahrenheit: .2f} grados fahrenheit son {nuevos_centigrados: .2f} grados centigrados")


if __name__ == "__main__":
    principal()
    