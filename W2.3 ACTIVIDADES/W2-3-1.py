# Ejercicio resuelto por © Alejandro Guerra Abán
# Haz un programa que pida la calificación por pantalla de un alumno (SB, NT, B, S, IN) y según se indique en la tabla adjunta se imprima "La calificación es xxxxxx" ejm SB sería "La calificación es SOBRESALIENTE".

calificacion = input("Introduce la calificación del alumno (SB, NT, B, S, IN): ")

if (calificacion == "SB"):
    print("La calificación es SOBRESALIENTE")
elif (calificacion == "NT"):
    print("La calificación es NOTABLE")
elif (calificacion == "B"):
    print("La calificación es BIEN")
elif (calificacion == "S"):
    print("La calificación es SUFICIENTE")
elif (calificacion == "IN"):
    print("La calificación es INSUFICIENTE")
else:
    print("Calificación no válida")