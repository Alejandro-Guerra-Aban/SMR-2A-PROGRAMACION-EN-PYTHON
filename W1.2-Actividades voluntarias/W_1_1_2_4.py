# Ejercicio W1-1.4 resuelto por Alejandro Guerra Abán

CONVERSORPESETA = 166.386

euros = float(input("Introduce la cantidad en euros: "))
eurosapesetas = euros * CONVERSORPESETA
print(f"{euros} euros son {eurosapesetas} pesetas.")

pesetas = float(input("Introduce la cantidad en pesetas: "))
pesetasaeuros = pesetas / CONVERSORPESETA
print(f"{pesetas} pesetas son {pesetasaeuros} euros.")