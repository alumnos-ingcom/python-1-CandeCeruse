################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio6 import ordenar_mayor_a_menor, ordenar_menor_a_mayor
"""
Test para funciones que ordenan de mayor a menor y de menor a mayor.
"""

def test_ordenar_mayor_a_menor():
    """
    Test orden contrario
    """
    uno = 1
    dos = 3
    tres = 5
    resultado = ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(resultado, tuple), "El resultado debe estar en una tupla"
    assert resultado == (5, 3, 1)
    
def test_ordenar_menor_a_mayor():
    """
    Test orden contrario
    """
    uno = 5
    dos = 3
    tres = 1
    resultado = ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(resultado, tuple), "El resultado debe estar en una tupla"
    assert resultado == ( 1, 3, 5)

