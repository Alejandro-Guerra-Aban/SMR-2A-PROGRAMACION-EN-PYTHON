# Ejercicio resuelto por © Alejandro Guerra Abán
# Escribe un programa que pregunte si llueve y si se tiene paraguas. Y que responda "me voy a mojar" o "no me voy a mojar" en función de los datos anteriores. La condición en una linea del if.

llueve = input("¿Está lloviendo? ")
paraguas = input("¿Tienes paraguas? ")

if (llueve == "si" and paraguas == "no"):
    print("Me voy a mojar")
else:
    print("No me voy a mojar")