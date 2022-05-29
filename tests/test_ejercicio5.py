################
# Candelaria Ceruse - @CandeCeruse
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio5 import signos, division_lenta
"""
Describir aquí que es lo que se esta probando.
Tengan en cuenta que el archivo tiene que llamarse igual
que el archivo a probar agregando antes `test_`
"""

def test_signos_ambos_positivos():
    """
    Caso de prueba ambos positivos
    """
    numero = 11
    otro_numero = 5
    dividendo, divisor, signo = signos(numero, otro_numero)
    assert isinstance (dividendo, int), "El divisor debe ser entero."
    assert isinstance (divisor, int), "El dividendo debe ser entero."
    assert isinstance (signo, int), "El signo debe ser entero."
    assert dividendo == 11, "El dividendo debe ser positivo"
    assert divisor == 5, "El divisor debe ser positivo."
    assert signo == 1, "El signo debe ser positivo."
    
def test_signos_ambos_negativos():
    """
    Caso de prueba ambos positivos
    """
    numero = -11
    otro_numero = -5
    dividendo, divisor, signo = signos(numero, otro_numero)
    assert isinstance (dividendo, int), "El divisor debe ser entero."
    assert isinstance (divisor, int), "El dividendo debe ser entero."
    assert isinstance (signo, int), "El signo debe ser entero."
    assert dividendo == 11, "El dividendo debe ser positivo"
    assert divisor == 5, "El divisor debe ser positivo."
    assert signo == 1, "El signo debe ser negativo."

def test_signos_dividendo_negativo():
    """
    Caso de prueba ambos negativos
    """
    numero = -11
    otro_numero = 5
    dividendo, divisor, signo = signos(numero, otro_numero)
    assert isinstance (dividendo, int), "El divisor debe ser entero."
    assert isinstance (divisor, int), "El dividendo debe ser entero."
    assert isinstance (signo, int), "El signo debe ser entero."
    assert dividendo == 11, "El dividendo debe ser positivo"
    assert divisor == 5, "El divisor debe ser positivo."
    assert signo == -1, "El signo debe ser negativo."
    
def test_signos_dividendo_negativo():
    """
    Caso de prueba con dividendo
    """
    numero = 11
    otro_numero = -5
    dividendo, divisor, signo = signos(numero, otro_numero)
    assert isinstance (dividendo, int), "El divisor debe ser entero."
    assert isinstance (divisor, int), "El dividendo debe ser entero."
    assert isinstance (signo, int), "El signo debe ser entero."
    assert dividendo == 11, "El dividendo debe ser positivo"
    assert divisor == 5, "El divisor debe ser positivo."
    assert signo == -1, "El signo debe ser negativo."
    
def test_signos_divisor_negativo():
    """
    Caso de prueba con divisor negativo.
    """
    numero = 11
    otro_numero = -5
    dividendo, divisor, signo = signos(numero, otro_numero)
    assert isinstance (dividendo, int), "El divisor debe ser entero."
    assert isinstance (divisor, int), "El dividendo debe ser entero."
    assert isinstance (signo, int), "El signo debe ser entero."
    assert dividendo == 11, "El dividendo debe ser positivo"
    assert divisor == 5, "El divisor debe ser positivo."
    assert signo == -1, "El signo debe ser negativo."
#-------------------------------------------------------------
def test_division_lenta_signo_positivo():
    """
    Caso de prueba cociente positivo
    """
    dividendo = 11
    divisor = 5
    signo = 1
    cociente, resto = division_lenta(dividendo, divisor, signo)
    assert isinstance (cociente, int), "El cociente debe ser entero."
    assert isinstance (resto, int), "El resto debe ser entero."
    assert isinstance (signo, int), "El signo debe ser entero."
    assert cociente == 2, "El dividendo debe ser positivo"
    assert resto == 1, "El divisor debe ser positivo."

def test_division_lenta_signo_negativo():
    """
    Caso de prueba cociente negativo
    """
    dividendo = 11
    divisor = 5
    signo = -1
    cociente, resto = division_lenta(dividendo, divisor, signo)
    assert isinstance (cociente, int), "El cociente debe ser entero."
    assert isinstance (resto, int), "El resto debe ser entero."
    assert isinstance (signo, int), "El signo debe ser entero."
    assert cociente == -2, "El dividendo debe ser positivo"
    assert resto == 1, "El divisor debe ser positivo."