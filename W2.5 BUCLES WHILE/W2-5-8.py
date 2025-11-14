# Ejercicio resuelto por © Alejandro Guerra Abán
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triangulo rectángulo como el de más abajo.
# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1

numero = int(input("Introduce un número entero positivo: "))
i = 1

while numero < 1:
    numero = int(input("Por favor, introduce un número entero positivo: "))
    
while i <= numero:
    j = i
    while j >= 1:
        print(j, end=" ")
        j -= 2
    print("")
    i += 2