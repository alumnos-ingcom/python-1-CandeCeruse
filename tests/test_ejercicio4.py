################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio4 import suma_lenta
"""
Escribir una función que haga la suma entre dos números
enteros sin hacer la operación de manera directa.
"""

def test_suma_lenta_a_y_b_positivos():
    """
    Caso de prueba ambos positivos
    """
    numero = 10
    otro_numero = 5
    resultado = suma_lenta(numero, otro_numero)
    assert isinstance (resultado, int), "El resultado debe ser entero."
    assert resultado == 15, "El resultado debe ser positivo y la suma correcta."

def test_suma_lenta_a_negativo_b_positivo():
    """
    Caso de prueba ambos positivos
    """
    numero = -10
    otro_numero = 5
    resultado = suma_lenta(numero, otro_numero)
    assert isinstance (resultado, int), "El resultado debe ser entero."
    assert resultado == -5, "El resultado debe ser negativo y la suma correcta."

def test_suma_lenta_a_positivo_b_negativo():
    """
    Caso de prueba ambos positivos
    """
    numero = 10
    otro_numero = -5
    resultado = suma_lenta(numero, otro_numero)
    assert isinstance (resultado, int), "El resultado debe ser entero."
    assert resultado == 5, "El resultado debe ser positivo y la resta correcta."

def test_suma_lenta_a_y_b_negativos():
    """
    Caso de prueba ambos positivos
    """
    numero = -10
    otro_numero = -5
    resultado = suma_lenta(numero, otro_numero)
    assert isinstance (resultado, int), "El resultado debe ser entero."
    assert resultado == -15, "El resultado debe ser negativo y la resta correcta."