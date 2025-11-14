# Ejercicio resuelto por © Alejandro Guerra Abán
# Escribe un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba "salir" que terminará.

entrada = ""

while entrada != "salir":
    entrada = input("Introduce un texto (escribe 'salir' para terminar): ")
    print(f"Eco: {entrada}")

while entrada == "salir":
    print("Has salido del programa.")
    break