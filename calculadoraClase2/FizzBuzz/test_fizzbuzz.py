import unittest
from FizzBuzz import FizzBuzz

class TestSumar(unittest.TestCase):
    def setUp(self):
        self.fb = FizzBuzz()

    def test(self):
        numero1 = 1
        resultadoEsperado = 1

        self.assertEqual(self.fb.fb_f(numero1), resultadoEsperado)

    def test(self):
        numero1 = 2
        resultadoEsperado = 2

        self.assertEqual(self.fb.fb_f(numero1), resultadoEsperado)

    def test(self):
        numero1 = 3
        resultadoEsperado = "Fizz"

        self.assertEqual(self.fb.fb_f(numero1), resultadoEsperado)

    def test(self):
        numero1 = 5
        resultadoEsperado = "Buzz"

        self.assertEqual(self.fb.fb_f(numero1), resultadoEsperado)

    def test(self):
        numero1 = 15
        resultadoEsperado = "FizzBuzz"

        self.assertEqual(self.fb.fb_f(numero1), resultadoEsperado)

if __name__ == '__main__':
    unittest.main()