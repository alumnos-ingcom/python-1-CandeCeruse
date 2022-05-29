################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio7 import sexadecimal_a_decimal, decimal_a_sexadecimal
"""
Esta funcion permite transformar un
número solicitado expresado en horas, minutos y
segundos a segundos a segundos. Y la otra que hace
el cambio en el sentido contrario, devolviendo una tuple.
"""

def test_sexadecimal_a_decimal():
    """
    Devuelve segundos.
    """
    horas = 2
    minutos = 36
    segundos = 65
    segundos = sexadecimal_a_decimal(horas, minutos, segundos)
    assert isinstance(segundos, int), "El resultado debe ser entero"
    assert segundos == 9425, "El resultado debe dar en segundos"

def test_decimal_a_sexadecimal():
    """
    Devuelve segundos.
    """
    segundos = 9425
    horas, minutos, segundos = decimal_a_sexadecimal(segundos)
    assert isinstance(horas, int), "El resultado debe ser entero"
    assert isinstance(minutos, int), "El resultado debe ser entero"
    assert isinstance(segundos, int), "El resultado debe ser entero"
    assert horas == 2, "El resultado debe dar en horas"
    assert minutos == 37, "El resultado debe dar en minutos"
    assert segundos == 5, "El resultado debe dar en segundos"
