print(
" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n"
"|					    		      |\n"
"|		ALEJANDRO GUERRA ABÁN			      |\n"
"|							      |\n"
"|	REALIZANDO [© ALEJANDRO GUERRA ABÁN 2025]             |\n"
"|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|\n"
      )

print("Definicion del ejercicio: Crea un sistema de ventas de entradas usando variables, usando una variable con el saludo, otra con el nombre, otra con el precio y una última para calcular el precio final de las entradas en caso de que el cliente compre más de una. El resultado debera imprimir usando prints el ticket que saldria una vez el pago se haya realizado.")

print()
print()

precio_ticket = 0
precio_final_entradas = 0

print("Formulario de datos:")

nombre = str(input("Introduce tu nombre: "))
print()
saludo = print(f"Buenos dias/tardes/noches", nombre)

print()
print()

print("Datos del evento:")

concierto = input("Introduce el nombre del concierto al que queires asistir: ")
print(f"Has seleccionado el concierto de {concierto}")

print()

print("Proceso de compra:")
print()
print("Precio de la entrada 20€")
print()

entradas = 0
PRECIO_TICKET = int(20)

entradas = int(input("¿Cuántas entradas quieres comprar? "))

print()

print("Se ha añadido las entrada al carrito.")

print("Has comprado en total:", PRECIO_TICKET)

print()

print("Carrito:")

carrito_normal = PRECIO_TICKET * entradas

print(f"El precio final de tu pedido es: {carrito_normal}€")

print()

print("Finalizacion del ejercicio")

print()

print("RESULTADO DEL EJERCICIO")

print()

print("*"*40)

print("ENTRADAS")
print()
print("Nombre: " + nombre)
print("Concierto seleccionado: " + concierto)
print("Total de entradas adquiridas: " + str(entradas))
print("Precio final a pagar: " + str(carrito_normal) + "€")
print()
print("© Alejandro Guerra Abán 2025")

print("*"*40)
