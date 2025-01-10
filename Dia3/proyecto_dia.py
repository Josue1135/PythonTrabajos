#Programar: Analizador de texto
#Programa que pide usuario un texto
#Programa pide al usuario que ingrese 3 letras a su eleccion
#codigo debe hacer 5 tipos de analisis con el fin de devolver la informacion:
#1. Cuantas veces aparecen las letras que eligio - (pasa todo a minuscula)almacenar letras en una lista
#2. Cuantas palabras hay en total
#3. Cual es la primera y ultima letra
#4. Poner el texto al inverso
#5. Programa debe decir si la palabra Python esta en el texto
from itertools import count

print("---------------------------------------")

texto = input("Usuario ingrese su texto a analizar: ")

print("---------------------------------------")

print("Texto ingresado para analizar:\n "+"<<"+texto+">>")

print("---------------------------------------")

print("Usuario ingrese 3 letas a analizar:\n ")
letras_1 = input("letra 1: ")
letras_2 = input("letra 2: ")
letras_3 = input("letra 3: ")

print("---------------------------------------------------------------------------------------------------")
print("Letras para analizar en el texto: " +"<< "+letras_1+" >>","<< "+letras_2+" >>", "<< "+letras_3+" >>")
print("---------------------------------------------------------------------------------------------------")

print("Analizando texto...\n"*3)
print("En el texto existen palabras en mayusculas, convirtiendo a minusculas...")
print("---------------------------------------------------------------------------------------------------")
texto_minuscula = texto.lower()
print("Texto convertido...\n" + "<< " +texto_minuscula+ " >>")
print("---------------------------------------------------------------------------------------------------")
print("Contando letras...\n"*2)
print("Total de letras en el texto: ")
print(len(texto_minuscula))
print("---------------------------------------------------------------------------------------------------")
print("Mostrando resultado...")
















