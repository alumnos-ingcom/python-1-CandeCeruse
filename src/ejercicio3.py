################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
3. Comparación de números

Escribir una función que utilizando sumas y restas, reciba dos valores y retorne:

    Retornar -1 si el primero es menor que el segundo
    Retornar 0 si son iguales
    Retornar 1 si el primero es mayor que el segundo

"""
#Funciones del ejercicio
def compara(numero, otro_numero):
    """
    Esta función resta el otro_numero a numero. Luego
    compara el resultado de esa resta y si es igual a cero significa
    que son iguales. Si es mayor que cero numero es mayor que otro_numero.
    Pero si el resultado es menor que cero, entonces otro_numero es mayor.
    """
    restados = numero - otro_numero
    if restados == 0:
        print(0)
        print("Son iguales")
    else:
        if restados > 0:
            print(1)
            print(f"{numero} es mayor que {otro_numero}")
        else:
            print(-1)
            print(f"{numero} es menor que {otro_numero}")

def principal():
    """
    Despues de ingresar ambos numeros, se resta numero_b al numero_a.
    Si da cero significa que son iguales.
    Si da mayor que cero es porque numero_a es mas grande que numero_b.
    Y sino se cumplen las condiciones anteriores, numero_b es mayor que numero_a.
    """
    numero_a = float(input("Ingrese numero a: "))
    numero_b = float(input("Ingrese numero b: "))
    compara(numero_a, numero_b)

if __name__ == "__main__":
    principal()
