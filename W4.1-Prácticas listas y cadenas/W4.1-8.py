# Ejercicio resuelto por © Alejandro Guerra Abán
# Haz un programa que pida una palabra la usuario, si empieza por h (mayúscual o minúscula) imprimirá: “La palabra xxxx empieza por h” y si no imprimirá “La palabra xxxxx no empieza por h”

palabra = input("Introduce una palabra: ")

if palabra.lower().startswith('h'): # Usamos el método lower para convertir la palabra a minúsculas y el método startswith para comprobar si la palabra empieza por 'h'.
    print("La palabra", palabra, "empieza por h")
else:
    print("La palabra", palabra, "no empieza por h")