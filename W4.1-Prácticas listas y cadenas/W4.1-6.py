# Ejercicio resuelto por © Alejandro Guerra Abán
# Haz un programa que pida al usuario una palabra y le responda con el número de letras que tiene, el programa continua hasta que el usuario escriba fin

palabra = input("Introduce una palabra (escribe 'fin' para terminar): ")

while palabra != "fin":
    print("La palabra", palabra, "tiene", len(palabra), "letras.")
    palabra = input("Introduce una palabra (escribe 'fin' para terminar): ")
print("Programa terminado.")
    