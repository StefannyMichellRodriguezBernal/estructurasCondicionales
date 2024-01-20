
Palabra1 = (input("ingrese una palabra:\n"))
palabra2 = (input("ingrese una palabra:\n"))
if len(Palabra1) > len(palabra2): 
    resta= (len (Palabra1) - len(palabra2))
    print (f"la palabra {Palabra1} tiene {resta} letras mas que {palabra2}")

elif len(palabra2) > len(Palabra1):
    resta = (len(palabra2)- len(Palabra1))
    print(f"la palabra{palabra2} tiene {resta} letras mas que {Palabra1}")
    
else:
    print(f"la palabra{Palabra1} tiene la misma cantidad de letras que {palabra2}")

