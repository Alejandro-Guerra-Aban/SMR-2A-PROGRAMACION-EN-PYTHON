# Ejercicio W1-1.7 resuelto por Alejandro Guerra Abán

dias = int(input("Introduce un número de días: "))

# semanas = dias // 7
# meses = dias // 30

# print(f"{dias} día/as son {semanas} semana/as o {meses} mes/es.")

meses = dias // 30
resto_dias = dias % 30
semanas = resto_dias // 7

print(f"{dias} día/as son {meses} mes/es y {semanas} semana/as")