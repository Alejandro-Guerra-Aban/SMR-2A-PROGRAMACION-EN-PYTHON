# Ejercicio resuleto por: © Alejandro Guerra Abán
# 3. Pedir al usuario dos números (comprobar que son números enteros) y escribir una función que imprima todos los números entre los números dados. La función debe verificar cuál es mayor para imprimirlos correctamente.

bien = False

while not bien:
    try:
        numero1 = input("Introduce el primer número entero: ")
        numero2 = input("Introduce el segundo número entero: ")
        numero1 = int(numero1)
        numero2 = int(numero2)
        bien = True
    except:
        print("Error: Debes introducir números enteros.")

def imprimir_numeros_entre(numero1, numero2):
    if numero1 < numero2:
        for i in range(numero1 + 1, numero2):
            print(i)
    else:
        for i in range(numero2 + 1, numero1):
            print(i)
imprimir_numeros_entre(numero1, numero2)