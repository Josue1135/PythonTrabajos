from xml.sax.handler import property_interning_dict

mascota = 'conejo'
if mascota == 'gato':
    print('La mascota es gato')
elif mascota == 'perro':
    print('La mascota es perro')
else:
    print('no se que mascota tienes')



num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))


if num1 > num2:
    print(f"{num1} es mayor que {num2}")
if num2 > num1:
    print(f"{num2} es mayor que {num1}")
if num1 == num2:
    print(f"{num1} y {num2} son iguales")



edad = 19
tiene_licencia = False

if edad > 18 and tiene_licencia == True:
    print("Puedes conducir")
if edad < 18 and tiene_licencia == False:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
if edad > 18 and tiene_licencia == False:
    print("No puedes conducir. Necesitas contar con una licencia")


habla_ingles = True
sabe_python = False

if habla_ingles == True and sabe_python == True:
    print("Cumples con los requisitos para postularte")
if sabe_python == False and habla_ingles == False:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
if sabe_python == True and habla_ingles == False:
    print("Para postularte, necesitas tener conocimientos de inglés")
if sabe_python == False and habla_ingles == True:
    print("Para postularte, necesitas saber programar en Python")







