################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio2 import signo
"""
Estos son los test correspondienets al archivo `ejercicio1.py` que esta en
`src`. Escribir una función que reciba un número e indique si el mismo es positivo,
negativo o cero utilizando sumas y restas.
"""

def test_signo_positivo():
    """
       Una breve descripción del caso de prueba aplicado a la función
    """
    numero = 10
    resultado = signo(numero)
    assert isinstance (resultado, int), "El resultado debe ser entero"
    assert resultado == 1, "El resultado debe ser positivo"

def test_signo_negativo():
    """
       Una breve descripción del caso de prueba aplicado a la función
    """
    numero = -10
    resultado = signo(numero)
    assert isinstance (resultado, int), "El resultado debe ser entero"
    assert resultado == -1, "El resultado debe ser negativo"

def test_signo_cero():
    """
       Una breve descripción del caso de prueba aplicado a la función
    """
    numero = 0
    resultado = signo(numero)
    assert isinstance (resultado, int), "El resultado debe ser entero"
    assert resultado == 0, "El resultado debe ser cero"   
