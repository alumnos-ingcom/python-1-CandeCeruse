################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio8 import es_primo
"""
Casos de prueba par numero primos
"""

def test_es_primo():
    """
    Numero primo
    """
    numero = 73
    resultado, respuesta_booleana = es_primo(numero)
    assert isinstance(respuesta_booleana, bool), "El resultado debe ser booleano"
    assert respuesta_booleana == True, "El resultado debe ser True"

def test_no_es_primo():
    """
    No es primo
    """
    numero = 48
    resultado, respuesta_booleana = es_primo(numero)
    assert isinstance(respuesta_booleana, bool), "El resultado debe ser booleano"
    assert respuesta_booleana == False, "El resultado debe ser False"