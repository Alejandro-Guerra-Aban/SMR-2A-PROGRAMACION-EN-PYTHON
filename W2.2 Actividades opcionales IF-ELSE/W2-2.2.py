# Ejercicio resuelto por © Alejandro Guerra Abán
# Escribe un programa que pida el salario y si es un jefe o un empleado (J/E).
# · Si es jefe y cobra menos de 2000 euros se le sube un 10% el sueldo.
# · Si es empleado y cobra menos de 1500 euros se le sube un 10% el sueldo.
# · Tiene que escribir: "Se le sube el sueldo un 10%" o "No se le sube el sueldo"

salario = float(input("Introduce el salario: "))
tipo = input("¿Es jefe o empleado? (J/E): ")

if (tipo == "J" or "j" and salario < 2000) or (tipo == "E" or "e" and salario < 1500):
    print("Se le sube el sueldo un 10%")
else:
    print("No se le sube el sueldo")
