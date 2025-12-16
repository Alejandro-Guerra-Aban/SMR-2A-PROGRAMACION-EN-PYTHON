# Ejercicio resuelto por © Alejandro Guerra Abán
# Escribir un programa que alamacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

contraseña = "secreto"

bien = False

while not bien:
    try:
        entrada = input("Introduce la contraseña: ")
        bien = True
    except:
        print("Entrada no válida. Inténtalo de nuevo.")

for i in range(100):  # Bucle grande para permitir muchos intentos
    if entrada == contraseña:
        print("Contraseña correcta. Acceso concedido.")
        break
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")
        try:
            entrada = input("Introduce la contraseña: ")
        except:
            print("Entrada no válida. Inténtalo de nuevo.")