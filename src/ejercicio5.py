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

def signo_dividendo(dividendo):
    '''
    Cambia el signo si el dividendo es negativo
    '''
    if dividendo < 0:
        print("\nCambio de signo dividendo")
        dividendo = dividendo * -1 #lo hago positivo para que no haga quilombo
        print(f"Dividendo= {dividendo}")
    return dividendo

def signo_divisor(divisor):
    '''
    Cambia el signo si el divisor es negativo
    '''
    if divisor < 0:
        print("\nCambio de signo divisor")
        divisor = divisor * -1 #lo hago positivo para que no haga quilombo
        print(f"Divisor= {divisor}\n")
    return divisor

def division_lenta(dividendo, divisor, dividendo_original, divisor_original):
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
            print(f"     = {dividendo}")
            cociente = cociente + 1 #sumo cada vez que el divisor entre en el dividendo
            continue
        print("-------------")   
        print(f"{dividendo_original} / {divisor_original} = {cociente}")
        print(f"Resto = {dividendo}")
        

def principal():
    """
    
    """
    dividendo = int(input("Ingrese divisor: "))
    divisor = int(input("Ingrese dividendo: "))
    
    dividendo_original = dividendo
    divisor_original = divisor
    '''
    Guardo las variables originales
    '''
    dividendo_positivo = signo_dividendo(dividendo)
    divisor_positivo = signo_divisor(divisor)
    division_lenta(dividendo_positivo, divisor_positivo, dividendo_original, divisor_original)
    pass

if __name__ == "__main__":
    principal()

"""
Fin de ejercicio
"""