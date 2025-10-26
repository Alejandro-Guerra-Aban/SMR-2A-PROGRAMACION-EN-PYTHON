# Ejercicio resuelto por © Alejandro Guerra Abán
# Escribe un programa que pida el numero de productos que ha comprado y si alguno está de promoción. Si tiene descuento imprimir "Tiene descuento", si no tiene descuento imprimir "No tiene descuento", poner las condiciones del descuento en un solo if.
# Las condiciones del descuento son:
# · Si ha comrpado menos de 3 no tiene descuento.
# · Si ha comprado 3 o 4 tiene descuento a no ser que alguno esté de promoción.
# · Si ha comprado 5 o más tiene descuento aunque tenga promociones.

num_productos = int(input("¿Cuántos productos ha comprado? "))
promocion = input("¿Alguno de los productos está de promoción? ")

if (num_productos >= 5) or (num_productos >= 3 and promocion == "no"):
    print("Tiene descuento")
else:
    print("No tiene descuento")