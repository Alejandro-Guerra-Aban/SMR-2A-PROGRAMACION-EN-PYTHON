# Ejercicio resuelto por © Alejandro Guerra Abán
# Escriba un programa que pida un año y que escriba si es bisiesto o no. Un año es bisiesto si es divisible por 4. Sin embargo, si un año es divisible por 100, no es bisiesto, a menos que también sea divisible por 400.  Ejemplo: El año 2000 fue bisiesto porque es divisible por 400, pero el 2100 no será bisiesto porque, aunque es divisible por 100, no lo es por 400.

año = int(input("Introduce un año: "))

if (año % 400 == 0) or (año % 4 == 0 and año % 100 != 0):
    print("El año", año, "es bisiesto")
else:
    print("El año", año, "no es bisiesto")