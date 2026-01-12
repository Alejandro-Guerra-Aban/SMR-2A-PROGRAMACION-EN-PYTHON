# Ejercicio resuelto por © Alejandro Guerra Abán
# Haz un programa que pida al usuario una palabra y le responda con la palabra en mayúsculas y las letras a sustituidas por 4, el programa continua hasta que el usuario escriba fin

palabra = input("Introduce una palabra (escribe 'fin' para terminar): ")

while palabra != "fin":
    palabra_modificada = palabra.upper().replace('A', '4') # Usamos el método lower para convertir la palabra a minúsculas y el método replace para sustituir las letras 'a' que al ser modificadas por mayusculas debemos remplanzar 'A' por '4'.
    print("Palabra modificada:", palabra_modificada)
    palabra = input("Introduce una palabra (escribe 'fin' para terminar): ")
print("Programa terminado.")
