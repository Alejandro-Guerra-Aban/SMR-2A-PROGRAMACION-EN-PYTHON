# Ejercicio W1-1.1 resuelto por Alejandro Guerra Abán

IVA = int(21)

precio_pantalon = int(input("Introduce el precio del pantalón: "))
numero_pantalones = int(input("Introduce el número de pantalones: "))
precio_gersey = int(input("Introduce el precio del gersey: "))
numero_gersys = int(input("Introduce el número de gersys: "))

print(f"He comproado {numero_pantalones} pantalones con {precio_pantalon}€ y {numero_gersys} gersys por {precio_gersey}€.")
precio_total = (precio_pantalon * numero_pantalones) + (precio_gersey * numero_gersys)
print(f"El precio total es de {precio_total}€.")
iva_total = (precio_total * IVA) / 100
print(f"El IVA es de {iva_total}€.")
precio_final = precio_total + iva_total
print(f"El precio final es de {precio_final}€.")