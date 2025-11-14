# Ejercicio resuelto por © Alejandro Guerra Abán
# Escribir un programa que alamacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

contraseña = "secreto"
entrada = input("Introduce la contraseña: ")

while entrada != contraseña:
    entrada = input("Contraseña incorrecta. \nIntroduce la contraseña: ")
print("Contraseña correcta. \n¡Acceso concedido!")