# Ejercicio W1-1.5 resuelto por Alejandro Guerra Abán

IVA = int(21)

numero_surtidor = int(input("Introduce el número de surtidor (1-4): "))
producto = input("Introduce el producto: ")
litros = float(input("Introduce los litros vendidos: "))
precio_por_litro = float(input("Introduce el precio por litro: "))

importe = litros * precio_por_litro
b_imponible = importe / (1 + IVA / 100)
imp_iva = importe - b_imponible


print("FACTURA SIMPLIFICADA")
print(f"Surtidor: {numero_surtidor}")
print(f"Producto: {producto}")
print(f"Litros: {litros}")
print(f"Precio litro: {precio_por_litro}")
print(f"Importe: {importe}")
print("-" * 60)
print(f"IVA: {IVA}%")
print(f"B imponible: {b_imponible}")
print(f"Imp. IVA: {imp_iva}")