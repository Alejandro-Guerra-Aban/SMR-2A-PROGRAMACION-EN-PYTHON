# Modulo creado por: © Alejandro Guerra Abán
# En este modulo se recopilan todas las funciones utilizadas en las practicas de W3.1

def saludo_simple(n):
    """Muestra 'hola' el número de veces indicado por n."""
    for i in range(n):
        print("Hola")

def saludo_nombre(n, nombre):
    """Muestra 'Hola [nombre]' el número de veces indicado por n."""
    for i in range(n):
        print(f"Hola {nombre}")

def imprimir_rango(numero1, numero2):
    """Imprime los números situados entre numero1 y numero2, sin incluirlos."""
    if numero1 < numero2:
        for i in range(numero1 + 1, numero2):
            print(i)
    else:
        for i in range(numero2 + 1, numero1):
            print(i)

def calcular_circulo(radio, operacion):
    """
    Calcula área o perímetro según el radio y operación indicada.
    Usa el valor pi = 3.1416
    """
    pi = 3.1416
    operacion = operacion.lower()
    
    if operacion == "área" or operacion == "area":
        resultado = pi * radio ** 2
        print(f"El área del círculo es: {resultado}")
    elif operacion == "perimetro" or operacion == "perímetro":
        resultado = 2 * pi * radio
        print(f"El perímetro del círculo es: {resultado}")
    else:
        print("Error: Operación no válida. Debes elegir 'área' o 'perímetro'.")

def devolver_maximo(numero1, numero2):
    """Devuelve el mayor de dos números."""
    if numero1 > numero2:
        return numero1
    else:
        return numero2