# Ejercicio resuelto por © Alejandro Guerra Abán
# Descripción del ejercicio: Haz un programa que pida dos lados de un rectángulo, su área y su perímetro. Si el área es correcta que imprima "El área es correcta" y sino que imprima "El área no es correcta", lo mismo con el perímetro.

lado1 = float(input("Introduce el primer lado del rectángulo: "))
lado2 = float(input("Introduce el segundo lado del rectángulo: "))

area_usuario = float(input("Introduce el área del rectángulo: "))
perimetro_usuario = float(input("Introduce el perímetro del rectángulo: "))

area_calculada = lado1 * lado2
perimetro_calculado = 2 * (lado1 + lado2)

if (area_usuario == area_calculada):
    print("El área es correcta")
else:
    print("El área no es correcta")

if (perimetro_usuario == perimetro_calculado):
    print("El perímetro es correcto")
else:
    print("El perímetro no es correcto")