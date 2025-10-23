# Ejercicio resuelto por © Alejandro Guerra Abán
# Descripción del ejercicio: Haz un programa que pida una clave y la guarde. Luego pide confirmar la clave. Si la clave es igual a la guardada que imprima "acceso autorizado" si es distinta que imprima "acceso no autorizado"

clave_guardada = input("Introduce una clave: ")
clave_confirmar = input("Confirma la clave: ")

if (clave_guardada == clave_confirmar):
    print("Acceso autorizado")
else:
    print("Acceso no autorizado")