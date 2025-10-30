# Ejercicio resuelto por © Alejandro Guerra Abán
# Haz el mismo programa, en el que además de lo anterior para el caso INSUFUCIENTE además imprima NO APTO y para el resto imprima APTO

calificacion = input("Introduce la calificación del alumno (SB, NT, B, S, IN): ")

if (calificacion == "SB"):
    print("La calificación es SOBRESALIENTE")
    print("APTO")
elif (calificacion == "NT"):
    print("La calificación es NOTABLE")
    print("APTO")
elif (calificacion == "B"):
    print("La calificación es BIEN")
    print("APTO")
elif (calificacion == "S"):
    print("La calificación es SUFICIENTE")
    print("APTO")
elif (calificacion == "IN"):
    print("La calificación es INSUFICIENTE")
    print("NO APTO")
else:
    print("Calificación no válida")