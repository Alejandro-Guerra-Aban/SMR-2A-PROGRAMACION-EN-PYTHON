# Ejercicio resuelto por © Alejandro Guerra Abán
# Haz el mismo programa, en el que además de lo anterior para el caso INSUFUCIENTE además imprima NO APTO y para el resto imprima APTO

calificacion = input("Introduce la calificación del alumno (SB, NT, B, S, IN): ")

match calificacion:
    case "SB":
        print("La calificación es SOBRESALIENTE")
        print("APTO")
    case "NT":
        print("La calificación es NOTABLE")
        print("APTO")
    case "B":
        print("La calificación es BIEN")
        print("APTO")
    case "S":
        print("La calificación es SUFICIENTE")
        print("APTO")
    case "IN":
        print("La calificación es INSUFICIENTE")
        print("NO APTO")
    case _:
        print("Calificación no válida")