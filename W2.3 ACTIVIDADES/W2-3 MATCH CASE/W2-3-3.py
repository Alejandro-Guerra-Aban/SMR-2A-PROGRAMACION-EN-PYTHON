# Ejercicio resuelto por © Alejandro Guerra Abán
# Haz el mimso programa pidiendo las notas como números enteros

calificacion = int(input("Introduce la calificación del alumno: "))

match calificacion:
    case 9 | 10:
        print("La calificación es SOBRESALIENTE")
        print("APTO")
    case 7 | 8:
        print("La calificación es NOTABLE")
        print("APTO")
    case 6:
        print("La calificación es BIEN")
        print("APTO")
    case 5:
        print("La calificación es SUFICIENTE")
        print("APTO")
    case 0 | 1 | 2 | 3 | 4:
        print("La calificación es INSUFICIENTE")
        print("NO APTO")
    case _:
        print("Calificación no válida")