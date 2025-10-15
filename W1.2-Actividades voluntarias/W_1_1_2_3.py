# Ejercicio W1-1.3 resuelto por Alejandro Guerra Abán

a = int(20)
b = int(40)

# Realice las mismas operaciones pero usando variables para guardar los resultados y luego muestre las variables
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
potencia = a ** b
resto = a % b

print("Resultado de la suma:" , suma)
print("Resultado de la resta:" , resta)
print("Resultado de la multiplicación:" , multiplicacion)
print("Resultado de la división:" , division)
print("Resultado de la potencia:" , potencia)
print("Resultado del resto:" , resto)


# Muestre el resultado de la suma, resta, multiplicacion, divison, potencia y resto de la division, con un texto indicando la operacion: "El resultado de la suma de voloreda y valordeb es: xxxxxxx"
print(f"El resultado de la suma de {a} y {b} es: {a + b}")
print(f"El resultado de la resta de {a} y {b} es: {a - b}")
print(f"El resultado de la multiplicación de {a} y {b} es: {a * b}")
print(f"El resultado de la división de {a} y {b} es: { a / b}")
print(f"El resultado de la potencia de {a} y {b} es: { a ** b}")
print(f"El resultado del resto de la división de {a} y {b} es: { a % b}")
