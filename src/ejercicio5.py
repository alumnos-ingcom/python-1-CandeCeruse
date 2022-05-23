################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
5. Divisiones

Escribir una función que mediante restas sucesivas,
obtenga el valor del cociente y resto de dos números enteros.
"""
# Funciones del ejercicio

def signos(dividendo, divisor):
    '''
    Cambia el signo si alguno es negativo
    '''
    if dividendo < 0 and divisor < 0:
        dividendo = dividendo * -1 #lo hago positivo para que no haga quilombo
        divisor = divisor * -1 #lo hago positivo para que no haga quilombo
        signo = 1
    elif dividendo < 0:
        print("\nCambio de signo dividendo")
        dividendo = dividendo * -1 #lo hago positivo para que no haga quilombo
        signo = -1
        print(f"Dividendo= {dividendo}")
        
    elif divisor < 0:
        print("\nCambio de signo divisor")
        divisor = divisor * -1 #lo hago positivo para que no haga quilombo
        signo = -1
        print(f"Divisor= {dividendo}")
    else:
        signo = 1
    return dividendo, divisor, signo


def division_lenta(dividendo, divisor, signo, dividendo_original, divisor_original):
    '''
    Funcion responsable de hacer las restas sucesivas.
    Los datos ingresados ya fueron filtrados por las funciones
    de cambio de signo.
    '''
    cociente = 0
    
    if divisor == 0:
        print("No se puede dividir por cero")
        
    else:
        print("\nFuncion division lenta: ")
        while dividendo >= divisor:
            print(f"{dividendo} - {divisor}")
            dividendo = dividendo - divisor
            cociente = cociente + 1 #sumo cada vez que el divisor entre en el dividendo
            print(f"Resto = {dividendo}")
        cociente = cociente * signo
        print("-------------")
        print("Resultado: \n")
        print(f"{dividendo_original} / {divisor_original} = {cociente}")
        print(f"Resto = {dividendo}")
  

def principal():
    """
    Este programa toma los datos ingresados y les cambia el signo
    si son negativos. Luego analiza si el dividendo es cero, si no lo es
    empieza las restas sucesivas para conseguir el cociente y el resto.
    Una vez que no se puede restar el divisor al dividendo el programa
    termina y muestra los resultados.
    
    """
    dividendo = int(input("Ingrese dividendo: "))
    divisor = int(input("Ingrese divisor: "))
    
    dividendo_original = dividendo
    divisor_original = divisor
    '''
    Guardo las variables originales
    '''
    dividendo_positivo, divisor_positivo, signo = signos(dividendo, divisor)
    
    division_lenta(dividendo_positivo, divisor_positivo, signo, dividendo_original, divisor_original)

    pass

if __name__ == "__main__":
    principal()

"""
Fin de ejercicio
"""