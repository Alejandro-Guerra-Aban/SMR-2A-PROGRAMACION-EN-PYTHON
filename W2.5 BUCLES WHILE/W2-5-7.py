# Ejercicio resuelto por © Alejandro Guerra Abán
# Escribe un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

numero = 1

while numero <= 10:
    multiplicador = 1
    while multiplicador <= 10:
        print(f"{numero} x {multiplicador} = {numero * multiplicador}")
        multiplicador += 1
    print("")
    numero += 1