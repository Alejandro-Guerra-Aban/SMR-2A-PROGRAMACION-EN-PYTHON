# Ejercicio resuelto por © Alejandro Guerra Abán
# Haz el mismo programa del ejercicio 2 pero que el cálculo del mayor se haga en la funcion mayor(lista)

numero = input("Introduce una lista de números enteros separados por espacios: ")

def mayor(lista):
    lista = [int(x) for x in lista.split()] # RECORDATORIO: En este caso lo que se esta realizando es convertir los números enteros de la lista creada por el usuario y ha cada valor de lista lo iremos comporando para ver si es el mayor y usando el metodo split para separar los números por espacios, y leugo podemos devolver la lsita definida por el usuario junto al número mayor.
    return max(lista)

print("La lista de números es:", numero)

print("El número mayor de la lista es:", mayor(numero))