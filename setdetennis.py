# Desarrolle un programa que solucione el problema de Solarrabietas:
def set_ganado(m, n):
    if m == n:
        return "No termina"
    if m == 7 and n <= 5:
        return "Gano A"
    if n == 7 and m <= 5:
        return "Gano B"
    if n == 6 and m <= 4:
        return "Gano A"
    if n == 6 and m <= 4:
        return "Gano B"
    if n == 5 and m <= 3:
        return "Gano A"
    if n == 5 and m <= 3:
         return "Gano B"
    return "aun no termina"


m = int(input("ingrese el numero de los juegos ganados por el jugador A: "))
n = int(input("ingrese el numero de los juegos ganados por el jugador B: "))


print(set_ganado(m, n))
    
        
            
        

 
   


