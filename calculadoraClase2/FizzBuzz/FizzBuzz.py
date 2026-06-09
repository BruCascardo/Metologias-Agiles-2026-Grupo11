class FizzBuzz:
    """
    def fb_f (self, a):

        Codigo generado con TDD
        if a == 3:
            return "Fizz"
        elif a == 5:
            return "Buzz"
        elif a == 15:
            return "FizzBuzz"
        else:
            return a
        """

    def fb_f(self, a):
        if a % 3 == 0 and a % 5 == 0:
            return "FizzBuzz"
        elif a % 3 == 0:
            return "Fizz"
        elif a % 5 == 0:
            return "Buzz"
        else:
            return a


if __name__ == '__main__':
    fb = FizzBuzz
