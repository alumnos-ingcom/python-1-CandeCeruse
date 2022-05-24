################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
4. Suma lenta

Escribir una función que haga la suma entre dos números
enteros sin hacer la operación de manera directa.
Esto quiere decir que para hacer la suma entre 4 y 3,
las operaciones resultantes deberán ser 4+1+1+1.

La funcion debe ser capaz de sumar cualquier numero entero positivo y negativo.
"""
#Funciones del ejercicio

def suma_lenta(numero, otro_numero):
    '''
    Si otro_numero es positivo, todo bien.
    Sino que en vez de sumar, lo reste.
    '''
    if otro_numero < 0 :
        print(f"{numero} + ({otro_numero})")
        otro_numero=otro_numero * -1

        while otro_numero > 0:
            numero=numero-1
            otro_numero-=1
            print(f"+ (-1) = {numero}")
    else:
        print(f"{numero} + {otro_numero}")
        while otro_numero > 0:
            otro_numero-=1
            numero=numero+1
            print(f"+1 = {numero}")

    print(f"Total = {numero}")

def principal():
    """
    Despues de ingresar dos numeros, la funcion suma_lenta los sumara
    de a uno. Si el segundo numero es negativo la suma se convierte en
    una resta.
    """
    numero_a = int(input("Ingrese numero a: "))
    numero_b = int(input("Ingrese numero b: "))
    suma_lenta(numero_a, numero_b)


if __name__ == "__main__":
    principal()
