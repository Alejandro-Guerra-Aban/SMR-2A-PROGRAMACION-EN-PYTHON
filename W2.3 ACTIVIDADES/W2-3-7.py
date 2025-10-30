# Ejercicio resuelto por © Alejandro Guerra Abán
# Pide el mes del año e indica la estación del año: Primavera, Verano, Otoño o Invierno. Ejemplo de salida: En enero es invierno

mes = input("Introduce el mes del año: ")

if (mes == "enero" or mes == "febrero" or mes == "diciembre"):
    print("En", mes, "es invierno")
elif (mes == "marzo" or mes == "abril" or mes == "mayo"):
    print("En", mes, "es primavera")
elif (mes == "junio" or mes == "julio" or mes == "agosto"):
    print("En", mes, "es verano")
elif (mes == "septiembre" or mes == "octubre" or mes == "noviembre"):
    print("En", mes, "es otoño")
else:
    print("Mes no válido")