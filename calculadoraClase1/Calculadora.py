class Calculadora:
    def sumar(self, a, b):
        return a+b

    def restar(self, a, b):
        return a-b

    def multiplicar(self, a, b):
        return a*b

    def dividir(self, a, b):
        if b == 0:
            return "Error: No se puede dividir por cero."
        return a/b


if __name__ == "__main__":
    c = Calculadora()
    opc = input("Seleccione la operación (1 - sumar, 2 - restar, 3 - multiplicar, 4 - dividir): ")

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opc == "1":
        resultado = c.sumar(num1, num2)
        opc_nombre = "suma"
    elif opc == "2":
        resultado = c.restar(num1, num2)
        opc_nombre = "resta"
    elif opc == "3":
        resultado = c.multiplicar(num1, num2)
        opc_nombre = "multiplicación"
    elif opc == "4":
        resultado = c.dividir(num1, num2)
        opc_nombre = "división"
    else:
        print("Operación no válida.")
        exit()

    print(f"El resultado de la {opc_nombre} es: {resultado}")
