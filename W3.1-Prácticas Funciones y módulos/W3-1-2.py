# Ejercicio resuleto por: © Alejandro Guerra Abán
# 2. Escribir un programa con la función saludo, igual que el anterior pero indicando también el nombre de la persona y muestra n veces “Hola Aranxa”
bien = False
while not bien:
    try:
        nombre = input("¿Cómo te llamas?: ")
        bien = True
    except:
        print("Entrada no válida. Inténtalo de nuevo.")
        
def saludo (n, nombre):
    bien2 = False
    while not bien2:
        try:
            n = int(input("¿Cuántas veces quieres que te salude?: "))
            bien2 = True
        except:
            print("Entrada no válida. Inténtalo de nuevo.")
    for i in range(n):
        print(f"Hola {nombre}")
saludo(0, nombre)