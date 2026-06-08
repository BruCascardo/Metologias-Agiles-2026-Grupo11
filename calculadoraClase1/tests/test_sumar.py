"""Tests unitarios para el método sumar de la clase Calculadora"""
import unittest
from Calculadora import Calculadora


class TestSumar(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_sumar_positivos(self):
        self.assertEqual(self.calc.sumar(2, 3), 5)

    def test_sumar_ceros(self):
        self.assertEqual(self.calc.sumar(0, 0), 0)

    def test_sumar_positivo_negativo(self):
        self.assertEqual(self.calc.sumar(-1, 1), 0)

    def test_sumar_negativos(self):
        self.assertEqual(self.calc.sumar(-5, -3), -8)

    def test_sumar_numeros_grandes(self):
        self.assertEqual(self.calc.sumar(10, 20), 30)

    def test_sumar_numeros_muy_grandes(self):
        self.assertEqual(self.calc.sumar(100, 200), 300)

    def test_sumar_negativo_positivo(self):
        self.assertEqual(self.calc.sumar(-10, 5), -5)

    def test_sumar_otro_positivo(self):
        self.assertEqual(self.calc.sumar(7, 8), 15)

    def test_sumar_decimales(self):
        self.assertEqual(self.calc.sumar(0.5, 0.5), 1.0)

    def test_sumar_opuestos_grandes(self):
        self.assertEqual(self.calc.sumar(-100, 100), 0)

if __name__ == '__main__':
    unittest.main()
