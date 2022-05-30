################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio2 import signo
"""
Estos son los test correspondienets al archivo `ejercicio2.py` que esta en
`src`. Es una función que recibe un número e indica si el mismo es positivo,
negativo o cero utilizando sumas y restas.
"""

def test_signo_positivo():
    """
    Comprueba si el numero es negativo.
    """
    numero = 10
    resultado = signo(numero)
    assert isinstance (resultado, int), "El resultado debe ser entero"
    assert resultado == 1, "El resultado debe ser positivo"

def test_signo_negativo():
    """
    Comprueba si el numero es negativo
    """
    numero = -10
    resultado = signo(numero)
    assert isinstance (resultado, int), "El resultado debe ser entero"
    assert resultado == -1, "El resultado debe ser negativo"

def test_signo_cero():
    """
    Comprueba su el numero es cero.
    """
    numero = 0
    resultado = signo(numero)
    assert isinstance (resultado, int), "El resultado debe ser entero"
    assert resultado == 0, "El resultado debe ser cero"   
