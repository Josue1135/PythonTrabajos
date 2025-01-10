#upper
#
from multiprocessing.forkserver import read_signed
from xml.sax.handler import property_interning_dict

texto = "Esto es un texto, Josue"
resultado = texto
print(texto)
print("---------------------------------------")
print("----1---")
texto2 = "Esto es un texto, Josue 2"
resultado2 = texto2[2].upper()
print(resultado2)
resultado2 = texto2.upper()
print(resultado2)

print("---------------------------------------")
print("----2-SPLIT -> SEPARAR--")
texto3 = "Esto es otro texto, Josue"
resultado3 = texto3.split()
print(resultado3)
resultado3 = texto3.split("t")
print(resultado3)

print("---------------------------------------")
print("----3- LOWER -> TODO EN MINUSCULA --")
texto4 = "Esto es otro texto, Josue"
resultado4 = texto4.lower()
print(resultado4)

print("---------------------------------------")
print("---4----")
texto5 = "Esto es otro texto, Josue 50"
resultado5 = texto5.lower()
print(resultado5)

print("---------------------------------------")
print("---5-JOIN-> UNIR---")
a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a, b, c, d])
print(e)

print("---------------------------------------")
print("---6--> FIND ES BUSCAR->cuando no encuestra arroja el -1 ")
texto6 = "Esto es otro texto, Josue 6"
resultado6 = texto6.find("t")
print(resultado6)


print("---------------------------------------")
print("-----7 REPLACE -> REEMPLAZAR")
texto7 = "Esto es otro texto, Josue 7"
print(texto7)
resultado7 = texto7.replace("Josue", "Moroni Vera")
print(resultado7)

#Práctica Métodos de String 1
# Imprime el siguiente texto en mayúsculas, empleando el método específico de strings:

frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
nuevo = frase.upper()
print(nuevo)

#Une la siguiente lista en un string, separando cada elemento con un espacio.
# Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado.

lista_palabras = ["La","legibilidad","cuenta."]
nueva = " ".join(["La", "legibilidad", "cuenta."])
print(nueva)

#Reemplaza en la siguiente frase:
# "Si la implementación es difícil de explicar, puede que sea una mala idea."
# los siguientes pares de palabras:
# "difícil" --> "fácil"
# "mala" --> "buena"
# y muestra en pantalla la frase con ambas palabras modificadas.

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
nueva = frase.replace("difícil", "fácil")
nueva2 = nueva.replace("mala", "buena")
print(nueva2)

