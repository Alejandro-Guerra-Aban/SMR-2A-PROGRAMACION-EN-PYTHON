# Ejercicio resuelto por © Alejandro Guerra Abán
# Crea la funcion suma y la función media, que tengan como parámetro una lista de números y devuelvan la suma y la media aritmética. Pruebalo con la lista de números enteros [5, 13, 24, 9, 43, 2, 19, 5, 24]

numero = [5, 13, 24, 9, 43, 2, 19, 5, 24]

def suma(lista):
    return sum(lista)

def media(lista):
    return suma(lista) / len(lista) # Usamos el método len para obtener la cadena de números en la lista y dividir la suma entre esa cantidad.

print("La lista de números es:", numero)

print("La suma de los números de la lista es:", suma(numero))
print("La media aritmética de los números de la lista es:", media(numero))