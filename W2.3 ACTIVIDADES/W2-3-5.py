# Ejercicio resuelto por © Alejandro Guerra Abán
# Haz el mismo programa en el que además si el importe total es más de 50€ haga un descuento del 5%. La salida será igual que la anterior añadiendo:
#   Descuento xxxxxx
#   Improte final xxxxxx

# Y si no hay descuento:
#   Sin descuento


producto = input("Introduce el tipo de producto (SP/98, SP/95, DS/A, DS/B): ")
litros = float(input("Introduce los litros a repostar: "))

if (producto == "SP/98"):
    print("Producto: SP/98")
    print("Precio por litro: 1,99€")
    importe_total = litros * 1.99
    if importe_total > 50:
        descuento = importe_total * 0.05
        importe_final = importe_total - descuento
        print("Descuento: " + str(descuento) + "€")
        print("Importe final: " + str(importe_final) + "€")
    else:
        print("Sin descuento")
elif (producto == "SP/95"):
    print("Producto: SP/95")
    print("Precio por litro: 1,69€")
    importe_total = litros * 1.69
    if importe_total > 50:
        descuento = importe_total * 0.05
        importe_final = importe_total - descuento
        print("Descuento: " + str(descuento) + "€")
        print("Importe final: " + str(importe_final) + "€")
    else:
        print("Sin descuento")
elif (producto == "DS/A"):
    print("Producto: DS/A")
    print("Precio por litro: 1,59€")
    importe_total = litros * 1.59
    if importe_total > 50:
        descuento = importe_total * 0.05
        importe_final = importe_total - descuento
        print("Descuento: " + str(descuento) + "€")
        print("Importe final: " + str(importe_final) + "€")
    else:
        print("Sin descuento")
elif (producto == "DS/B"):
    print("Producto: DS/B")
    print("Precio por litro: 1,95€")
    importe_total = litros * 1.95
    if importe_total > 50:
        descuento = importe_total * 0.05
        importe_final = importe_total - descuento
        print("Descuento: " + str(descuento) + "€")
        print("Importe final: " + str(importe_final) + "€")
    else:
        print("Sin descuento")
else:
    print("Producto no válido")