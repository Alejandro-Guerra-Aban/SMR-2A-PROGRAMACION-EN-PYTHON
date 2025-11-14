# Ejercicio resuelto por © Alejandro Guerra Abán
# Escribe un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números imapres desde 1 hasta ese número separados por comas.

numero = int(input("Introduce un número entero positivo: "))

impar = 1

while impar < numero:
    print(impar, end=", ")
    impar += 2