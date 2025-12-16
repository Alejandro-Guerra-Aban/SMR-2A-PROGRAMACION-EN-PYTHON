# Ejercicio resuelto por © Alejandro Guerra Abán
# Programa para calcular la factura de una gasolinera usando for

# Precios por tipo de producto
precio_sp98 = 1.99
precio_sp95 = 1.69
precio_dsA = 1.59
precio_dsB = 1.35

bien = False

while not bien:
    try:
        num_facturas = int(input("¿Cuántas facturas quieres hacer?: "))
        bien = True
    except:
        print("Entrada no válida. Inténtalo de nuevo.")

for i in range(num_facturas):
    print(f"\nFactura {i + 1}")
    tipo_producto = input("Introduce el tipo de producto (SP/98, SP/95, DS/A, DS/B): ")
    litros = float(input("Introduce los litros vendidos: "))

    if tipo_producto == "SP/98":
        precio_litro = precio_sp98
    elif tipo_producto == "SP/95":
        precio_litro = precio_sp95
    elif tipo_producto == "DS/A":
        precio_litro = precio_dsA
    elif tipo_producto == "DS/B":
        precio_litro = precio_dsB
    else:
        print("Tipo de producto no válido.")
        continue  # pasa a la siguiente iteración del for

    importe_total = precio_litro * litros

    print("\n--- FACTURA ---")
    print(f"Producto: {tipo_producto}")
    print(f"Precio por litro: {precio_litro} €")
    print(f"Litros: {litros}")
    print(f"Importe total: {importe_total} €")
    print("----------------")
