# Escriba un programa que simule una calculadora básica, este puede realizar operación de suma, resta, multiplicación y división.
numero1 = float(input("ingresa el primer numero: "))
numero2 = float(input("ingresa el segundo numero: "))
operador = (input("ingresa el operador (+, -, *, /): "))

if operador == "+":
    resultado = numero1 + numero2
elif operador == "-":
    resultado = numero1 - numero2
elif operador == "*":
    resultado = numero1 * numero2
elif operador == "/":
    resultado = numero1 / numero2

else:
    print("operador no valido")

if operador in "+-*/":
    print(f"el resultado de la operacion {numero1} {operador} {numero2} es: {resultado}")
    