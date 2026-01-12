# Ejercicio resuelto por © Alejandro Guerra Abán
# Haz el mismo programa pidiendo al usuario la lista de números enteros separados por espacios, que imprima la lista y devuelva el mayor.

numero = input("Introduce una lista de números enteros separados por espacios: ")
numero = [int(x) for x in numero.split()] # RECORDATORIO: En este caso lo que se esta realizando es convertir los números enteros de la lista creada por el usuario y ha cada valor de lista lo iremos comporando para ver si es el mayor y usando el metodo split para separar los números por espacios, y leugo podemos devolver la lsita definida por el usuario junto al número mayor.

maximo = max(numero)

print("La lista de números es:", numero)

print("El número mayor de la lista es:", maximo)