# Ejercicio resuelto por © Alejandro Guerra Abán
# Pide el mes del año e indica la estación del año: Primavera, Verano, Otoño o Invierno. Ejemplo de salida: En enero es invierno

mes = input("Introduce el mes del año: ")

match mes:

    case "enero" | "febrero" | "diciembre":
        print("En", mes, "es invierno")
    case "marzo" | "abril" | "mayo":
        print("En", mes, "es primavera")
    case "junio" | "julio" | "agosto":
        print("En", mes, "es verano")
    case "septiembre" | "octubre" | "noviembre":
        print("En", mes, "es otoño")
    case _:
        print("Mes no válido")