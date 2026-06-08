"""Tests unitarios para el método multiplicar de la clase Calculadora"""
import unittest
from Calculadora import Calculadora


class TestMultiplicar(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_multiplicar_positivos(self):
        self.assertEqual(self.calc.multiplicar(2, 3), 6)

    def test_multiplicar_por_cero(self):
        self.assertEqual(self.calc.multiplicar(0, 0), 0)

    def test_multiplicar_positivo_negativo(self):
        self.assertEqual(self.calc.multiplicar(-1, 1), -1)

    def test_multiplicar_negativos(self):
        self.assertEqual(self.calc.multiplicar(-5, -3), 15)

    def test_multiplicar_numeros_medianos(self):
        self.assertEqual(self.calc.multiplicar(10, 20), 200)

    def test_multiplicar_numeros_grandes(self):
        self.assertEqual(self.calc.multiplicar(100, 200), 20000)

    def test_multiplicar_negativo_positivo(self):
        self.assertEqual(self.calc.multiplicar(-10, 5), -50)

    def test_multiplicar_otro_positivo(self):
        self.assertEqual(self.calc.multiplicar(7, 8), 56)

    def test_multiplicar_decimales(self):
        self.assertEqual(self.calc.multiplicar(0.5, 0.5), 0.25)

    def test_multiplicar_opuestos_grandes(self):
        self.assertEqual(self.calc.multiplicar(-100, 100), -10000)


if __name__ == '__main__':
    unittest.main()
