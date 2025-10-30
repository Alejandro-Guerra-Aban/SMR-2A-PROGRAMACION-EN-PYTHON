# Ejercicio resuelto por © Alejandro Guerra Abán
# Haz un programa de Gasolinera que pida el tipo de producto y los litros y te imprima el producto, precio por litro e importe total. Siendo los preios y productos:
#     SP/98 - 1,99€
#     SP/95 - 1,69€
#     DS/A - 1,59€
#     DS/B - 1,95€

producto = input("Introduce el tipo de producto (SP/98, SP/95, DS/A, DS/B): ")
litros = float(input("Introduce los litros a repostar: "))

if (producto == "SP/98"):
    print("Producto: SP/98")
    print("Precio por litro: 1,99€")
    importe_total = litros * 1.99
    print("Importe total: " + str(importe_total) + "€")
elif (producto == "SP/95"):
    print("Producto: SP/95")
    print("Precio por litro: 1,69€")
    importe_total = litros * 1.69
    print("Importe total: " + str(importe_total) + "€")
elif (producto == "DS/A"):
    print("Producto: DS/A")
    print("Precio por litro: 1,59€")
    importe_total = litros * 1.59
    print("Importe total: " + str(importe_total) + "€")
elif (producto == "DS/B"):
    print("Producto: DS/B")
    print("Precio por litro: 1,95€")
    importe_total = litros * 1.95
    print("Importe total: " + str(importe_total) + "€")
else:
    print("Producto no válido")