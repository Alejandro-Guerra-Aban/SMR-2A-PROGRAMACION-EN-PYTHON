for i in range(2,9,2):
    print(i)
    
for j in range(6, -4, -3):
    print(j)
    
try :
    edad = int(input("edad: "))
except:
    print("debe ingresar un numero")
    edad=0
print(edad)