# Ejercicio resuelto por © Alejandro Guerra Abán
# Descripción del ejercicio: Haz un programa que pida un número entero entre 1 y 10. Si el número esta fuera de ese rango que imprima "número fuera de rango", si el número está dentro del rango que imprima "El número es xxxxxxxxx" siendo xxxxxxxxx el número.

numero = int(input("Introduce un número entre 1 y 10: "))

if (numero < 1 or numero > 10):
    print("Número fuera de rango")
else:
    print("El número es", numero)