# 1. Contador simple:
# Imprime los números del 1 al 10 usando un while.

print("\nImprime los números del 1 al 10 usando un while.\n")

contador = 1

while contador <= 10:
    print(contador)
    contador += 1
    
print("Fin del contador simple.\n")
    
# 2. Cuenta regresiva:
# Pide un número al usuario y muestra una cuenta atrás hasta 0.

print("\nPide un número al usuario y muestra una cuenta atrás hasta 0.\n")

numero = int(input("Ingresa un número para la cuenta regresiva: "))

while numero >= 0:
    print(numero)
    numero -= 1
    
print("Fin de la cuenta regresiva.\n")
    
# 3. Suma acumulada:
# Pide números al usuario hasta que introduzca un 0. Muestra la suma total.

print("\nPide números al usuario hasta que introduzca un 0. Muestra la suma total.\n")

numero = int(input("Ingresa un número (0 para terminar): "))
suma = 0

while numero != 0:
    suma += numero
    numero = int(input("Ingresa un número (0 para terminar): "))
print("La suma total es:", suma)

print("Fin del programa de suma acumulada.\n")

# 4. Validación de entrada:
# Pide al usuario una contraseña hasta que escriba “python”.

print("\nPide al usuario una contraseña hasta que escriba “python”.\n")

contraseña = "python"

entrada = input("Ingresa la contraseña: ")

while entrada != contraseña:
    entrada = input("Contraseña incorrecta.\nIngresa la contraseña: ")
print("Contraseña correcta.\nAcceso concedido.")

print("Fin del programa de validación de entrada.\n")

# 5. Números pares:
# Muestra los números pares del 2 al 20 con un while.

print("\nMuestra los números pares del 2 al 20 con un while.\n")

numero = 2

while numero <= 20:
    print(numero)
    numero += 2
    
print("Fin del programa de números pares.\n")

# 6. Adivina el número:
# El programa tiene un número secreto. El usuario intenta adivinarlo y el bucle continúa hasta que lo logre.

print("\nEl programa tiene un número secreto. El usuario intenta adivinarlo y el bucle continúa hasta que lo logre.\n")

numero_secreto = 10

adivinanza = int(input("Advinia el número secreto: "))

while adivinanza != numero_secreto:
    adivinanza = int(input("Incorrecto.\nIntenta de nuevo: "))
print("¡Correcto! Has adivinado el número secreto.")

print("Fin del programa de adivina el número.\n")

# 7. Contador de dígitos:
# Pide un número y usa while para contar cuántos dígitos tiene.

print("\nPide un número y usa while para contar cuántos dígitos tiene.\n")

numero = int(input("Ingresa un número para contar sus dígitos: "))

contador_digitos = 0

while numero != 0:
    numero //= 10
    contador_digitos += 1
print("El número tiene", contador_digitos, "dígitos.")

print("Fin del programa de contador de dígitos.\n")

# 8. Promedio de notas:
# Pide notas hasta que el usuario ingrese un número negativo. Calcula el promedio.

print("\nPide notas hasta que el usuario ingrese un número negativo. Calcula el promedio.\n")

suma_notas = 0
contador_notas = 0

nota = float(input("Ingresa una nota (negativa para terminar): "))

while nota >= 0:
    suma_notas += nota
    contador_notas += 1
    nota = float(input("Ingresa una nota (negativa para terminar): "))
if contador_notas > 0:
    promedio = suma_notas / contador_notas
    print("El promedio de las notas es:", promedio)
else:
    print("No se ingresaron notas válidas.")
    
print("Fin del programa de promedio de notas.\n")

# 9. Cajero automático simplificado:
# Menú repetitivo con while que permita: ingresar dinero, retirar, consultar saldo, salir.

print("\nMenú repetitivo con while que permita: ingresar dinero, retirar, consultar saldo, salir.\n")

saldo = 0
opcion = ""

while opcion != "4":
    print("\nMenú Cajero Automático:")
    print("1. Ingresar dinero")
    print("2. Retirar dinero")
    print("3. Consultar saldo")
    print("4. Salir")
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        ingreso = float(input("Ingresa la cantidad a depositar: "))
        saldo += ingreso
        print("Has depositado:", ingreso)
    elif opcion == "2":
        retiro = float(input("Ingresa la cantidad a retirar: "))
        if retiro <= saldo:
            saldo -= retiro
            print("Has retirado:", retiro)
        else:
            print("Saldo insuficiente.")
    elif opcion == "3":
        print("Tu saldo actual es:", saldo)
    elif opcion == "4":
        print("Saliendo del cajero automático.")
    else:
        print("Opción no válida. Intenta de nuevo.")
        
print("Fin del programa del cajero automático.\n")
        
# 10. Validación múltiple:
# Pide usuario y contraseña. Repite hasta que sean correctos, con un máximo de 3 intentos.

print("\nPide usuario y contraseña. Repite hasta que sean correctos, con un máximo de 3 intentos.\n")

usuarrio_correcto = "admin"
contraseña_correcta = "1234"
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    usuario = input("Ingresa el usuario: ")
    contraseña = input("Introduce la contraseña: ")
    if usuario == usuarrio_correcto and contraseña == contraseña_correcta:
        print("Acceso concedido.\nBinevneido al sistema.", usuario)
        break
    else:
        intentos += 1
        print("Usuario o contraseña incorrectos.\nIntento", intentos, "de", max_intentos)
    if intentos == max_intentos:
        print("Has excedido el número máximo de intentos.\nAcceso denegado.")
    else:
        print("Intenta de nuevo.\n")

print("Fin del programa de validación múltiple.\n")

# 10. Validación múltiple: (Versión 2)
# Pide usuario y contraseña. Repite hasta que sean correctos, con un máximo de 3 intentos.

print("\nPide usuario y contraseña. Repite hasta que sean correctos, con un máximo de 3 intentos.\n")

usuarrio_correcto = input("Define el usuario correcto: ")
contraseña_correcta = input("Define la contraseña correcta: ")
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    usuario = input("Ingresa el usuario: ")
    contraseña = input("Introduce la contraseña: ")
    if usuario == usuarrio_correcto and contraseña == contraseña_correcta:
        print("Acceso concedido.\nBinevneido al sistema.", usuario)
        break
    else:
        intentos += 1
        print("Usuario o contraseña incorrectos.\nIntento", intentos, "de", max_intentos)
    if intentos == max_intentos:
        print("Has excedido el número máximo de intentos.\nAcceso denegado.")
    else:
        print("Intenta de nuevo.\n")
        
print("Fin del programa de validación múltiple.\n")
        
# 11. Creación de menu de seleección + validación con match case
# Crea un menu de selección con una validación con match case.

print("\nCrea un menu de selección con una validación con match case.\n")
opcion = ""

while opcion != "C":
    print("\nMenú de Selección:")
    print("A. Pizza Margarita")
    print("B. Pizza Atún")
    print("C. Salir")
    
    opcion = input("Selecciona una opción: ")
    
    match opcion:
        case "A":
            print("Has seleccionado la Pizza Margarita.")
        case "B":
            print("Has seleccionado la Pizza de Atún.")
        case "C":
            print("Saliendo del menú.")
        case _:
            print("Opción no válida. Intenta de nuevo.")
print("Fin del programa de menú de selección.\n")