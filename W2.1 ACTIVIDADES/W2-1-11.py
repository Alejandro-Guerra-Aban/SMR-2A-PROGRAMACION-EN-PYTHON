# Ejercicio resuelto por © Alejandro Guerra Abán
# Descripción del ejercicio: Haz un programa que pida un número decimal que se guarde en un float y un número decimal que se guarda en un string. Si los números son iguales que imprima "Los números son iguales", si no que imprima "Los números son distintos"

numero = float(input("Introduce un número decimal: "))
numero_str = input("Introduce otro número decimal: ")

if (numero == float(numero_str)):
    print("Los números son iguales")
else:
    print("Los números son distintos")