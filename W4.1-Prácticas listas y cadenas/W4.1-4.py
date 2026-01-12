# Ejercicio resuelto por © Alejandro Guerra Abán
# Haz un programa que dada una lista de números enteros [5, 13, 24, 9, 43, 2, 19, 5, 24], que imprima la lista y devuelva la suma y la media aritmética (suma dividida entre la cantidad de números).

numero = [5, 13, 24, 9, 43, 2, 19, 5, 24]

suma_numeros = sum(numero)
media_aritmetica = suma_numeros / len(numero) # Usamos el método len para obtener la cadena de números en la lista y dividir la suma entre esa cantidad.

print("La lista de números es:", numero)

print("La suma de los números de la lista es:", suma_numeros)
print("La media aritmética de los números de la lista es:", media_aritmetica)