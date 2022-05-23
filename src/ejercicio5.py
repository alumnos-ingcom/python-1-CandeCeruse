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

def division_lenta(dividendo, divisor):
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
        print("-------------")
        print("Resultado: \n")
        print(f"Resto = {dividendo}")
        return cociente
        
        
def signo_cociente(cociente, dividendo_original, divisor_original):
    if divisor_original < 0 and dividendo_original < 0:
        pass
    elif divisor_original < 0 or dividendo_original < 0:
        cociente = cociente * -1
    print(f"{dividendo_original} / {divisor_original} = {cociente}")

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
    dividendo_positivo = signo_dividendo(dividendo)
    divisor_positivo = signo_divisor(divisor)
    
    cociente = division_lenta(dividendo_positivo, divisor_positivo)
    signo_cociente(cociente, dividendo_original, divisor_original)
    pass

if __name__ == "__main__":
    principal()

"""
Fin de ejercicio
"""