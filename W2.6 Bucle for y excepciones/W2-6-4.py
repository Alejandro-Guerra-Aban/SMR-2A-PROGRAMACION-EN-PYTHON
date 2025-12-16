# Ejercicio resuelto por © Alejandro Guerra Abán
# Escribe un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
bien = False

while not bien:
    try:
        numero = int(input("Introduce un número entero positivo: "))
        bien = True
    except:
        print("Entrada no válida. Inténtalo de nuevo.")
        
for i in range(numero, -1, -1):
    if i > 0:
        print(i, end=", ")
    else:
        print(i)