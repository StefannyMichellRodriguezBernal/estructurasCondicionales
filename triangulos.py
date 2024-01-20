# Escriba un programa que reciba como entrada los tres lados de un triángulo, e indique:
def tipo_triangulo(a, b, c):


    if a <= 0 or b <= 0 or c <= 0:
        return "No es un triangulo valido"
    
    if a + b <= c or a + c <= b or b + c <= a:
        return "No es un triangulo valido"
    
    if a == b or a == c or b == c:
        return "Es un triangulo isosceles"
    return "Es un triangulo escaleno"


a = float(input("ingrese el primer lado del triangulo: "))
b = float(input("ingrese el segundo lado del triangulo: "))
c = float(input("ingrese el tercer lado del triangulo: "))


print(tipo_triangulo(a, b, c))
