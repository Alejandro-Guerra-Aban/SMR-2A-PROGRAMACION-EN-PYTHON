# Ejercicio resuelto © Alejandro Guerra Abán
# Escribe un programa que pida al usuario un número entero positivo y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)

bien = False

while not bien:
    try:
        edad = int(input("Introduce su edad: "))
        bien = True
    except:
        print("Entrada no válida. Inténtalo de nuevo.")

for año in range(1, edad + 1):
    print(f"Has cumplido {año} años.")