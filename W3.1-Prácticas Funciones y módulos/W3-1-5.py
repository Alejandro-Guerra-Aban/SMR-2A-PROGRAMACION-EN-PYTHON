# Ejercicio resuleto por: © Alejandro Guerra Abán
# 5.  Pedir al usuario dos números y escribir una función que devuelva el máximo de los números y se imprima en el programa principal

bien = False

while not bien:
    try:
        numero1 = input("Introduce el primer número: ")
        numero2 = input("Introduce el segundo número: ")
        numero1 = int(numero1)
        numero2 = int(numero2)
        bien = True
    except:
        print("Error: Debes introducir números válidos.")

def devolver_maximo(numero1, numero2):
    if numero1 > numero2:
        return numero1
    else:
        return numero2
maximo = devolver_maximo(numero1, numero2)

print(f"El número máximo es: {maximo}")