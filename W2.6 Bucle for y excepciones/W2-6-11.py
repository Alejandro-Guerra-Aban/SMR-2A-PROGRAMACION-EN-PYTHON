# Ejercicio resuelto por © Alejandro Guerra Abán
# Escribe un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba "salir" que terminará.

entrada = ""

for i in range(1000):  # Bucle grande para permitir muchas entradas
    try:
        entrada = input("Introduce algo (escribe 'salir' para terminar): ")
    except:
        print("Entrada no válida. Inténtalo de nuevo.")
        continue

    if entrada.lower() == "salir":
        print("Programa terminado.")
        break
    else:
        print(f"Eco: {entrada}")