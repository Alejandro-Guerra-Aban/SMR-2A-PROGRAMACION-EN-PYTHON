# Ejercicio resuelto por © Alejandro Guerra Abán
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triangulo rectángulo como el de más abajo.
# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1

bien = False
while not bien:
    try:
        numero = int(input("Introduce un número entero positivo: "))
        i = 1
        bien = True
    except:
        print("Entrada no válida. Inténtalo de nuevo.")

for fila in range(1, numero + 1):
    for columna in range(fila):
        print(2 * (fila - columna) - 1, end=" ")
    print()

