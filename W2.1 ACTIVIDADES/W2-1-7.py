# Ejercicio resuelto por © Alejandro Guerra Abán
# Descripción del ejercicio: Haz un programa que pida dos lados de un rectángulo y su área. Si el área es correcta que imprima "El área es correcta"  y si no que imprima "El área no es correcta".

lado1 = float(input("Introduce el primer lado del rectángulo: "))
lado2 = float(input("Introduce el segundo lado del rectángulo: "))

area_usuario = float(input("Introduce el área del rectángulo: "))

area_calculada = lado1 * lado2

if (area_usuario == area_calculada):
    print("El área es correcta")
else:
    print("El área no es correcta")
