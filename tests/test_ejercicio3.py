################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio3 import compara
"""
Describir aquí que es lo que se esta probando.
Tengan en cuenta que el archivo tiene que llamarse igual
que el archivo a probar agregando antes `test_`
"""

def test_compara_numero_mayor_otronumero():
    """
    Caso de prueba para cuando el primer numero,
    es mayor que el segundo
    """
    numero = 10
    otro_numero = 5
    resultado = compara(numero, otro_numero)
    assert isinstance (resultado, int), "El resultado debe ser entero"
    assert resultado == 1, "El primero es mayor que el segundo"

def test_compara_otronumero_mayor_numero():
    """
    Caso de prueba para cuando el numero,
    es menor que el segundo
    """
    numero = 5
    otro_numero = 10
    resultado = compara(numero, otro_numero)
    assert isinstance (resultado, int), "El resultado debe ser entero"
    assert resultado == -1, "El primero debe ser menor que el segundo"

def test_compara_iguales():
    """
    Caso de prueba para cuando son iguales.
    """
    numero = 5
    otro_numero = 5
    resultado = compara(numero, otro_numero)
    assert isinstance (resultado, int), "El resultado debe ser entero"
    assert resultado == 0, "Deben ser iguales"
    