# Ejercico resuelto por: © Alejandro Guerra Abán
# 1. Escribir un programa con la función saludo, que pasa como parámetro el número de veces y muestra por pantalla “hola” ese número de veces. Se pide al usuario el número de veces a repetir el saludo(comprueba si es un número válido con excepciones)

def saludo (n):
    bien = False
    while not bien:
        try:
            n = int(input("¿Cuántas veces quieres que te salude?: "))
            bien = True
        except:
            print("Entrada no válida. Inténtalo de nuevo.")
    for i in range(n):
        print("Hola")
saludo(0)