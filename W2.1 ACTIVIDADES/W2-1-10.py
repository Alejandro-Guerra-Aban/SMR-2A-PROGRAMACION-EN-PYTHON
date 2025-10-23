# Ejercicio resuelto por © Alejandro Guerra Abán
# Descripción del ejercicio: Haz un programa que pida la categoría de un empleado, que puede ser A o B y el sueldo.
#   · Si la categoría es A, que aumente el sueldo un 10% e imprima "El sueldo era xxxxx y ahora es xxxxx"
#   · Si la categoría es B, que aumente el sueldo 500€ e imprima "El sueldo era xxxxx y ahora es xxxxx"

categoria = input("Introduce la categoría del empleado: ")
sueldo = float(input("Introduce el sueldo del empleado: "))

if (categoria == "A"):
    sueldo_nuevo = sueldo * 1.10
    print("El sueldo era", sueldo, "€ y ahora es", sueldo_nuevo, "€")
elif (categoria == "B"):
    sueldo_nuevo = sueldo + 500
    print("El sueldo era", sueldo, "€ y ahora es", sueldo_nuevo, "€")
else:
    print("Categoría no válida")