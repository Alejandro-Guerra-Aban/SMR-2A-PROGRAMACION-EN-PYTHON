# Ejercicio resuelto por © Alejandro Guerra Abán
# Escribe un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números imapres desde 1 hasta ese número separados por comas.

bien = False

while not bien:
    try:
        numero = int(input("Introduce un número entero positivo: "))
        bien = True
    except:
        print("Entrada no válida. Inténtalo de nuevo.")

for i in range(1, numero + 1, 2):
    if i < numero - 1:
        print(i, end=", ")
    else:
        print(i)