# Ejercicio resuelto © Alejandro Guerra Abán
# Haz un programa que pida al usuario una palabra y la muestre por pantalla 15 veces.

bien = False

while not bien:
    try:
        palabra = input("Introduce una palabra: ")
        bien = True
    except:
        print("Entrada no válida. Inténtalo de nuevo.")

for i in range(15):
    print(palabra)