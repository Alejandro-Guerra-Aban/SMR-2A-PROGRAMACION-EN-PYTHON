# Ejercicio resuelto por © Alejandro Guerra Abán
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
# *
# **
# ***
# ****
# *****

bien = False

while not bien:
    try:
        numero = int(input("Introduce un número: "))
        i = 1
        bien = True
    except:
        print("Entrada no válida. Inténtalo de nuevo.")

for i in range(1, numero + 1):
    print("*" * i)

