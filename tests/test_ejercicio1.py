################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio1 import convertir_a_fahrenheit, convertir_a_centigrados
"""
Estos son los test correspondienets al archivo `ejercicio1.py` que esta en
`src`
El programa convierte de grados centigrados a fahrenheit y viceversa.
Los test se aplicaran a el input, los grados centigrados.
"""

def test_convertir_a_fahrenheit_positivos():
    """
    Grados centigrados positivos
    """
    grados = 150
    resultado = convertir_a_fahrenheit(grados)
    assert isinstance(resultado, float), "El resultado debe ser un número flotante"
    assert resultado == 302.00, "El resultado debe ser correcto"

def test_convertir_a_fahrenheit_negativos():
    grados = -150
    resultado = convertir_a_fahrenheit(grados)
    assert isinstance(resultado, float), "El resultado debe ser un número flotante"
    assert resultado == -238.00, "El resultado debe ser negativo y correcto"

def test_convertir_a_centigrados_positivo():
    fahrenheit = 302.00
    resultado = convertir_a_centigrados(fahrenheit)
    assert isinstance(fahrenheit, float), "El resultado debe ser un número flotante"
    assert resultado == 150.00, "El resultado debe ser positivo y correcto"

def test_convertir_a_centigrados_negativo():
    fahrenheit = -238.00
    resultado = convertir_a_centigrados(fahrenheit)
    assert isinstance(fahrenheit, float), "El resultado debe ser un número flotante"
    assert resultado == -150.00, "El resultado debe ser negativo y correcto"    
    