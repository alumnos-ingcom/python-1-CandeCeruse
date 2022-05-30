###############
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
7. Transformación de un número

Escribir un programa que permita transformar un
número solicitado expresado en horas, minutos y
segundos a segundos a segundos. Y otra que haga
el cambio en el sentido contrario, devolviendo una tuple.

Recuerden que un grado son 60 minutos y un minuto son 60 segundos.
"""
# Funciones del ejercicio
def sexadecimal_a_decimal(horas, minutos, segundos):
    """
    Esta funcion convierte de horas, minutos y segundos a segundos
    """
    horas_segundos = (horas*60)*60
    minutos_segundos = minutos*60

    suma_segundos = segundos + minutos_segundos + horas_segundos
    return suma_segundos

def decimal_a_sexadecimal(segundos):
    """
    Transforma los segundos a sexagesimal dividiendo cada dígito del numero
    sexagesimal, y guardando los restos en horas, minutos y segundos
    """
    horas_segundos = segundos // 3600
    resto_horas = segundos % 3600
    minutos_segundos = resto_horas // 60
    resto_minutos = resto_horas % 60
    segundos_convertidos  = resto_minutos
    return horas_segundos, minutos_segundos, segundos_convertidos

def principal():
    """
    Este programa transforma la hora ingresada a segundos.
    Y luego la vuelve a transformar a sexagesimal.
    """
    horas = int(input("Ingrese horas: "))
    minutos = int(input("Ingrese minutos: "))
    segundos = int(input("Ingrese segundos: "))
    suma_segundos = sexadecimal_a_decimal(horas, minutos, segundos)
    print(f"Segundos: {suma_segundos}")
    horas_segundos, minutos_segundos, segundos_convertidos = decimal_a_sexadecimal(suma_segundos)
    print(f"Resultado: {horas_segundos}hs, {minutos_segundos}', {segundos_convertidos}''")

if __name__ == "__main__":
    principal()
