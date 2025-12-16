# Ejercicio resuelto por © Alejandro Guerra Abán
# Haz un programa que calcule el área de un circulo dado el radio por pantalla y al acabar pregunta si se quiere volver a calcular. (pi radio al cuadrado)

bien = False

while not bien:
    try:
        radio = float(input("Introduce el radio del círculo: "))
        bien = True
    except:
        print("Entrada no válida. Saliendo del programa.")
        
        
area = 3.1416 * radio ** 2
print("El área del círculo es:", area)

bien2 = False

while not bien2:
    try:
        volver = input("¿Quieres calcular otra área? (s/n): ")
        for respuesta in volver:
            if respuesta == 's' or respuesta == 'S':
                radio = float(input("Introduce el radio del círculo: "))
                area = 3.1416 * radio ** 2
                print("El área del círculo es:", area)
            else:
                print("¡Hasta luego!")
                break
            try:
                volver = input("¿Quieres calcular otra área? (s/n): ")
            except:
                print("Entrada no válida. Saliendo del programa.")
                break
        bien2 = True
    except:
        print("Entrada no válida. Inténtalo de nuevo.")