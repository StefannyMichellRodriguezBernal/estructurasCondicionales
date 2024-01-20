# Escriba un programa que reciba como entrada la estatura, el peso y la edad de una persona, y le entregue su condición de riesgo.
Altura = float(input("ingrese su altura: "))
Peso = float(input("ingrese su peso: "))
Age = int(input("ingrese su edad: "))

IMC = (Peso)/((Altura/100)**2)
if Age>=45:
    if IMC>=22:
        print("riesgo alto")
    else:
        print("riesgo medio")
elif 0<Age<45:
    if IMC>=22:
        print("riesgo medio")
    else:
        print("riesgo bajo")
else:
    print("ingrese una edad valida")
