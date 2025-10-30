# Ejercicio resuelto por © Alejandro Guerra Abán
# Haz un programa que pida la calificación por pantalla de un alumno (SB, NT, B, S, IN) y según se indique en la tabla adjunta se imprima "La calificación es xxxxxx" ejm SB sería "La calificación es SOBRESALIENTE".

calificacion = input("Introduce la calificación del alumno (SB, NT, B, S, IN): ")

match calificacion:
    case "SB":
        print("La calificación es SOBRESALIENTE")
    case "NT":
        print("La calificación es NOTABLE")
    case "B":
        print("La calificación es BIEN")
    case "S":
        print("La calificación es SUFICIENTE")
    case "IN":
        print("La calificación es INSUFICIENTE")
    case _:
        print("Calificación no válida")