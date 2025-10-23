# Ejercicio resuelto por © Alejandro Guerra Abán
# Descripción del ejercicio: Haz un programa que pida un número entero menor o igual a 10. Si el número es mayor que 10 que imprima "Número no válido El número es mayor que 10", si es menor o igual a 10 que imprima "El número es xxxxxxxxx" siendo xxxxxxxxx el número.

numero = int(input("Introduce un número menor o igual 10: "))

if (numero > 10):
    print("Número no valido. El número es mayor que 10")
else:
    print("El número es", numero)