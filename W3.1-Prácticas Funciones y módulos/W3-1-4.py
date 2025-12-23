# Ejercicio resuleto por: © Alejandro Guerra Abán
# 4. Pedir al usuario el radio y la operación (perímetro o área) y escribir una función que calcule e imprima el perímetro o el área del círculo.

bien = False

while not bien:
    try:
        radio = input("Introduce el radio del círculo: ")
        radio = float(radio)
        bien = True
    except:
        print("Error: Debes introducir un número válido para el radio.")

operacion = input("¿Quieres calcular el área o el perímetro? ")

def calcular_circulo(radio, operacion):
    if operacion == "área" or operacion == "area":
        area = 3.1416 * radio ** 2
        print(f"El área del circulo es: {area}")
    elif operacion == "perimetro" or operacion == "perímetro":
        perimetro = 2 * 3.1416 * radio
        print(f"El perímetro del circulo es: {perimetro}")
    else:
        print("Error: Operación no válida. Debes elegir 'área' o 'perímetro'.")
calcular_circulo(radio, operacion)
