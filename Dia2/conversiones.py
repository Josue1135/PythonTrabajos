#Situaciones implicitas

numero = 2
numero2 = 20.5

numero = numero + numero2

print(type(numero))
print(type(numero2))

#Situaciones explicitas
numero4= 5.8
print(numero4)
print(type(numero4))

numero5 = int(numero4)
print(numero5)
print(type(numero5))

edad = input("Ingresa la edad: ")
edad = int(edad)
nueva = 2 + edad
print("Tu nueva edad es: " + str(nueva))