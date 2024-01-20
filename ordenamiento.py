# Escriba un programa que reciba como entrada dos números, y los muestre ordenados de menor a mayor:
# A continuación, escriba otro programa que haga lo mismo con tres números:
# Finalmente, escriba un tercer programa que ordene cuatro números:
def bubble_sort(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista [j+1]:
                lista[j], lista[j+1], lista[j]

entrada_usuario = input("ingrese los numeros que desea ordenar (separados por espacios): ")


numeros = [int(num) for num in entrada_usuario.split()]


sorted(numeros)


print("\t ---LISTA ORDENADA--- ")
print(f"\n\t{sorted(numeros)}")
