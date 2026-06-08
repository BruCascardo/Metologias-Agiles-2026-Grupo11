"""Tests unitarios para el método dividir de la clase Calculadora"""
import unittest
from Calculadora import Calculadora


class TestDividir(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_dividir_positivos(self):
        self.assertEqual(self.calc.dividir(6, 2), 3)

    def test_dividir_por_cero(self):
        self.assertEqual(self.calc.dividir(6, 0), "Error: No se puede dividir por cero.")

    def test_dividir_positivo_negativo(self):
        self.assertEqual(self.calc.dividir(-1, 1), -1)

    def test_dividir_negativos(self):
        self.assertEqual(self.calc.dividir(-5, -1), 5)

    def test_dividir_numeros_medianos(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)

    def test_dividir_numeros_grandes(self):
        self.assertEqual(self.calc.dividir(100, 20), 5)

    def test_dividir_negativo_positivo(self):
        self.assertEqual(self.calc.dividir(-10, 5), -2)

    def test_dividir_resultado_decimal(self):
        self.assertEqual(self.calc.dividir(7, 8), 0.875)

    def test_dividir_decimales(self):
        self.assertEqual(self.calc.dividir(0.5, 0.5), 1.0)

    def test_dividir_opuestos_grandes(self):
        self.assertEqual(self.calc.dividir(-100, 100), -1)


if __name__ == '__main__':
    unittest.main()
