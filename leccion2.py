# Crearía el script funciones.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

# y los dos archivos de prueba, uno utilizando unittest y otro utilizando pytest:
# test_unittest.py

import unittest
from funciones import *

class TestFunciones(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)
        self.assertEqual(suma(-2, 3), 1)

    def test_resta(self):
        self.assertEqual(resta(5, 3), 2)
        self.assertEqual(resta(5, -3), 8)

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(2, 3), 6)
        self.assertEqual(multiplicacion(-2, 3), -6)

    def test_division(self):
        self.assertEqual(division(6, 3), 2)
        self.assertEqual(division(-6, 3), -2)
        with self.assertRaises(ValueError):
            division(6, 0)

# test_pytest.py

import pytest
from funciones import *

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-2, 3) == 1

def test_resta():
    assert resta(5, 3) == 2
    assert resta(5, -3) == 8

def test_multiplicacion():
    assert multiplicacion(2, 3) == 6
    assert multiplicacion(-2, 3) == -6

def test_division():
    assert division(6, 3) == 2
    assert division(-6, 3) == -2
    with pytest.raises(ValueError):
        division(6, 0)

# y para ejecutar estas pruebas, debo ejecutar python -m unittest test_unittest.py 
# para ejecutar las pruebas de unittest, o pytest test_pytest.py para ejecutar las pruebas de pytest.