# Ejercicio resuelto por © Alejandro Guerra Abán
# Haz un progrma que calcule el área de un círuclo dado el radio por pantalla y al acabar pregunta si se quiere volver a calucular. (PI radio al cuadrado)

radio = float(input("Introduce el radio del círculo: "))

area = 3.1416 * radio ** 2
print("El área del círculo es:", area)

volver = input("¿Quieres calcular otra área? (s/n): ")
while volver == "s":
    radio = float(input("Introduce el radio del círculo: "))
    area = 3.1416 * radio ** 2
    print("El área del círculo es:", area)
    volver = input("¿Quieres calcular otra área? (s/n): ")