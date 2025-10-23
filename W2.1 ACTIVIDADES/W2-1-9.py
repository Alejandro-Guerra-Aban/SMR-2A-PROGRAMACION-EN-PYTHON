# Ejercicio resuelto por © Alejandro Guerra Abán
# Descripción del ejercicio: Haz un programa que pida los lados de un rectángulo que tienen que ser múltiplos y el área.
#  · Si alguno de los lados no es múltiplo de 10 que imprima "El lado no es múltiplo de 10" y no calcule nada.
#  · Si los dos son múltiplos de diez que calcule el área.
#   ·  Si el área no coincide con el área dada, que imrprima "El área no es correcta"
#   ·  Si el área coincide que imprima "El área es correcta"

lado1 = float(input("Introduce el primer lado del rectángulo (múltiplo de 10): "))
lado2 = float(input("Introduce el segundo lado del rectángulo (múltiplo de 10): "))

area_usuario = float(input("Introduce el área del rectángulo: "))

if (lado1 % 10 != 0 or lado2 % 10 !=0):
    print("El lado no es múltiplo de 10")
else:
    area_calculada = lado1 * lado2

    if area_usuario == area_calculada:
        print("El área es correcta")
    else:
        print("El área no es correcta")