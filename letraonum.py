# Escriba un programa que determine si un caracter ingresado es letra, número, o ninguno de los dos. En caso que sea letra, determine si es mayúscula o minúscula.

caracter = input("ingresa un caracter: ")
if len (caracter) == 0:
    print("no ingresaste ningun caracter")

elif caracter.isalpha():
    if caracter.isupper():
        print(f"el caracter '{caracter}' es una letra mayuscula")
    else: 
        print(f"el caracter '{caracter}' es una letra minuscula")
elif caracter.isdigit():
    print(f"el caracter '{caracter}' es un numero")
else: 
    print(f"el caracter '{caracter}' no es una letra, numero")