# Ejercicio resuelto por © Alejandro Guerra Abán
# Haz el mimso programa pidiendo las notas como números enteros

calificacion = int(input("Introduce la calificación del alumno: "))

if (calificacion >= 9 and calificacion <= 10):
    print("La calificación es SOBRESALIENTE")
    print("APTO")
elif (calificacion >= 7 and calificacion < 9):
    print("La calificación es NOTABLE")
    print("APTO")
elif (calificacion >= 6 and calificacion < 7):
    print("La calificación es BIEN")
    print("APTO")
elif (calificacion >= 5 and calificacion < 6):
    print("La calificación es SUFICIENTE")
    print("APTO")
elif (calificacion >= 0 and calificacion < 5):
    print("La calificación es INSUFICIENTE")
    print("NO APTO")
else:
    print("Calificación no válida")