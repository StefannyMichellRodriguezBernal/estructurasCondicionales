#Escriba un programa que pida dos números enteros y que calcule la división, indicando si la división es exacta o no.
dividiendo = int(input("ingrese el dividendo (numero a dividir): "))
divisor = int(input("ingrese el divisor (numero que divide): "))

resultado = dividiendo / divisor 
resto = dividiendo % divisor 

if resto == 0: 
    print("la division es exacta.")
else:
    print("la division no es exacta.")

print("el resultado de la division es")
