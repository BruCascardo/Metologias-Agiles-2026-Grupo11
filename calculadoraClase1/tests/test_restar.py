"""Tests unitarios para el método restar de la clase Calculadora"""
import unittest
from Calculadora import Calculadora


class TestRestar(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_restar_positivos(self):
        self.assertEqual(self.calc.restar(5, 3), 2)

    def test_restar_ceros(self):
        self.assertEqual(self.calc.restar(0, 0), 0)

    def test_restar_positivo_negativo(self):
        self.assertEqual(self.calc.restar(-1, 1), -2)

    def test_restar_negativos(self):
        self.assertEqual(self.calc.restar(-5, -3), -2)

    def test_restar_numeros_medianos(self):
        self.assertEqual(self.calc.restar(10, 20), -10)

    def test_restar_numeros_grandes(self):
        self.assertEqual(self.calc.restar(100, 200), -100)

    def test_restar_negativo_positivo(self):
        self.assertEqual(self.calc.restar(-10, 5), -15)

    def test_restar_otro_positivo(self):
        self.assertEqual(self.calc.restar(7, 8), -1)

    def test_restar_decimales(self):
        self.assertEqual(self.calc.restar(0.5, 0.5), 0.0)

    def test_restar_opuestos_grandes(self):
        self.assertEqual(self.calc.restar(-100, 100), -200)


if __name__ == '__main__':
    unittest.main()
