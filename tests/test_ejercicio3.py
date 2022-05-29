################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio3 import compara
"""
Test dedicados a un programa que compara dos numeros.
Y devuelve 1 si el primero es mayor que el segundo.
-1 si el segundo es mayor. Y 0 si son iguales.
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
    