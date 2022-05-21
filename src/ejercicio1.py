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

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    '''Ingresar centigrados'''
    centigrados = int(input("Ingrese grados centigrados\n"))
    '''Hace las conversiones'''
    fahrenheit = convertir_a_fahrenheit(centigrados)
    nuevos_centigrados = convertir_a_centigrados(fahrenheit)
    '''Muestra resultados'''
    imprimir_resultado(nuevos_centigrados , fahrenheit)
    pass

'''FUNCIONES:'''

def convertir_a_fahrenheit(valor_a_convertir):
    convertido_a_fahrenheit = float(((valor_a_convertir * 9) / 5) + 32 )
    '''convierto de celsius a fahrenheit'''
    return convertido_a_fahrenheit

def convertir_a_centigrados(valor_a_convertir):
    convertido_a_centigrados = float(((valor_a_convertir - 32) * 5) / 9)
    '''convierto de fahrenheit a centigrados'''
    return convertido_a_centigrados

def imprimir_resultado(centigrados, fahrenheit):
    centigrados=str(centigrados)
    fahrenheit=str(fahrenheit)
    print(centigrados + " grados centigrados son " + fahrenheit + " grados fahrenheit")
    print(fahrenheit + " grados fahrenheit son " + centigrados + " grados centigrados")

if __name__ == "__main__":
    principal()
    