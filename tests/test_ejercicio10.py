################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio10 import es_palindromo
"""
Caso de prueba para palabras palindromas
"""

def test_es_palindromo():
    """
    Testea si es palindromo
    """
    palabra = "neuquen"
    resultado = es_palindromo(palabra)
    assert isinstance(resultado, bool), "El resultado debe ser booleana"
    assert resultado == True, "La palabra debe ser palindromo"