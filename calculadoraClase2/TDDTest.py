import unittest
from TDDCalculadora import Calculadora


class TestSumar(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_1(self):
        numero1 = 0
        numero2 = 0
        resultadoEsperado = 0

        self.assertEqual(self.calc.sumar(numero1, numero2), resultadoEsperado)

    def test_2(self):
        numero1 = 0
        numero2 = 1
        resultadoEsperado = 1

        self.assertEqual(self.calc.sumar(numero1, numero2), resultadoEsperado)

    def test_3(self):
        numero1 = 1
        numero2 = 0
        resultadoEsperado = 1

        self.assertEqual(self.calc.sumar(numero1, numero2), resultadoEsperado)


if __name__ == '__main__':
    unittest.main()
