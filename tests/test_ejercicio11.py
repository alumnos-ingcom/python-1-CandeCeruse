################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio11 import es_multiplo
"""
Test para una función que indica con True si un número entero
es multiplo de otro, utilizando sumas y restas.
"""

def test_es_multiplo():
    """
    Testea si un numero es multiplo de otro
    """
    numero = 6
    multiplo = 36
    resultado = es_multiplo(numero, multiplo)
    assert isinstance(resultado, bool), "El resultado debe ser booleana"
    assert resultado == True, "La numero debe ser multiplo."