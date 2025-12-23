# Ejercicio resuleto por: © Alejandro Guerra Abán
# 6. Escribir todas las funciones en el módulo funciones.py y llamarlas desde el ejercicio 6.

import modulos.funciones as mfn

mfn.saludo_simple(3)

print("---") # Separador visual

mfn.saludo_nombre(2, "Alejandro")

print("---")

mfn.imprimir_rango(3, 10)

print("---")

mfn.calcular_circulo(5, "área")

print("---")

mfn.calcular_circulo(5, "perímetro")

print("---")

resultado_max = mfn.devolver_maximo(10, 20)
print(f"El número máximo es: {resultado_max}")