# Ejercicio resuelto por © Alejandro Guerra Abán
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
# *
# **
# ***
# ****
# *****

numero = int(input("Introduce un número: "))
i = 1

while numero < 1:
    numero = int(input("Por favor, introduce un número entero positivo: "))
    

while i <= numero:
    print("*" * i)
    i += 1
