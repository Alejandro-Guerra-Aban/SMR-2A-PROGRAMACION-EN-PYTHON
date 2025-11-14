# Ejercicio resuelto por © Alejandro Guerra Abán
# Crea un menú de sistema usando elif

print("*" * 30)
print("A. Borrar fichero")
print("B. Dar de alta usuario")
print("C. Dar de baja usuario")
print("*" * 30)

elecccion = input("Elige una opción (A, B o C): ")

if (elecccion == "A"):
    print("Se han borrado los ficheros")
elif (elecccion == "B"):
    usuario = input("Introduce el nombre de usuario al que quieres dar de alta: ")
    print("MÉTODO 1: Se ha dado de alta al usuario", usuario)
    print("MÉTODO 2: Se ha dado de alta al usuario" + " " + usuario)
    print(f"MÉTODO 3: Se ha dado de alta al usuario {usuario}")
elif (elecccion == "C"):
    usuario_baja = input("Introduce el nombre de usuario al que quieres dar de baja: ")
    print("MÉTODO 1: Se ha dado de baja al usuario", usuario_baja)
    print("MÉTODO 2: Se ha dado de baja al usuario" + " " + usuario_baja)
    print(f"MÉTODO 3: Se ha dado de baja al usuario {usuario_baja}")
else:
    print("Elección erronea / No has elegido ninguna opción")