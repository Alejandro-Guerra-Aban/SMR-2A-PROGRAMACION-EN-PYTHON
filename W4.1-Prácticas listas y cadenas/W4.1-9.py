# Ejercicio resuelto por © Alejandro Guerra Abán
# Haz un programa que pida una palabra la usuario, y una función que calcule si la palabra empieza por vocal. Si empieza por vocal imprimirá: “La palabra xxxx empieza por vocal” y si no imprimirá “La palabra xxxxx no empieza por vocal”

palabra = input("Introduce una palabra: ")

def empieza_por_vocal(palabra):
    return palabra[0].lower() in 'aeiou' # Comprobamos si la primera letra de la palabra (convertida a minúscula) está en la cadena de vocales.
if empieza_por_vocal(palabra):
    print("La palabra", palabra, "empieza por vocal")
else:
    print("La palabra", palabra, "no empieza por vocal")