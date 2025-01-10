#Inmutables, no se pueden cambiar: puedo cambiar el
#contenido de la variable pero el string de por si directamente
#no se puede cambiar

nombre = "Josue"
#nombre[0] = "M"
print(nombre)

#concatenar
n1 = "Josue"
n2 = "Moroni"
print(n1 + n2)
print(n1 + " " + n2)
print((n1 + " " + n2 + " \n")*10)

#puede contener varias lineas de codigo

poema = """Mil holas para ustedes
como les va en esta calido dia
señores y señaras esto es un 
texto"""
print(poema)
print("ustedes" in poema)
print("señores" not in poema)
print(len(poema))

##Práctica Propiedades de Strings 1


# 15 veces el texto "Repetición" y muestra el
# resultado en pantalla. Por suerte, conoces que
# los strings son multiplicables y puedes realizar
# esta actividad de forma simple y elegante.

texto = "Repetición"
print((texto +"\n") * 5)

print("Repeticion\n" * 5)

#Verifica si la palabra "agua" no se encuentra en el siguiente haiku. Debes imprimir el booleano.

texto = """Tierra mojada
mis recuerdos de viaje,
entre las lluvias"""

print("agua" not in texto)

#Muestra en pantalla el largo (en números de caracteres) de la palabra electroencefalografista.
palabra = "electroencefalografista"
print(len(palabra))






