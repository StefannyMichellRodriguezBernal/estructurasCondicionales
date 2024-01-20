#Escriba un programa que indique si un año es bisiesto o no, teniendo en cuenta cuál era el calendario vigente en ese año:
año = int(input("ingresa un año: "))
if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
    print("el año ", año, "es bisiesto")
else: 
    print("el año", año, "no es bisiesto")
