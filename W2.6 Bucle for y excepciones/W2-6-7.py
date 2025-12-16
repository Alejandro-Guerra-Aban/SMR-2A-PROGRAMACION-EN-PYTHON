# Ejercicio resuelto por © Alejandro Guerra Abán
# Escribe un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

numero = 1

for numero in range(1, 11):
    for multiplicador in range(1, 11):
        print(f"{numero} x {multiplicador} = {numero * multiplicador}")
    print("")