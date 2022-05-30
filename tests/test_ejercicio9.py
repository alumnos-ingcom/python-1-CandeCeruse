################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio9 import factores_primos
"""
Este test encuentra los factores primos del número ingresado
"""

def test_factores_primos():
    numero = 50
    resultado = factores_primos(numero)
    assert isinstance(numero, int), "El valor de entrada debe ser un entero"
    assert isinstance(resultado, tuple), "El valor de salida debe ser una tupla"
    assert resultado == (2, 5, 5), "El valor de salida no es el esperado"
    assert numero >= 0, "El valor de entrada debe ser positivo"
