import unittest
from TDDCalculadora import Calculadora

class TestSumar(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test(self):
        numero1 = 0
        numero2 = 0
        resultadoEsperado = 0

        self.assertEqual(self.calc.sumar(numero1, numero2), resultadoEsperado)

    def test(self):
        numero1 = 0
        numero2 = 1
        resultadoEsperado = 1

        self.assertEqual(self.calc.sumar(numero1, numero2), resultadoEsperado)
        
    def test(self):
        numero1 = 1
        numero2 = 0
        resultadoEsperado = 1

        self.assertEqual(self.calc.sumar(numero1, numero2), resultadoEsperado)

if __name__ == '__main__':
    unittest.main()