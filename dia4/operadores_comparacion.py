mi_bboooll= 100==100
print(mi_bboooll)
booll='blanco'=='negro'
print(booll)

#combinaciones
mi_bolll = (4 < 5) and (5 > 6)
print(mi_bolll)
otro = 10 == 10 or 3 == 3
print(otro)
otros = 10 == 10 or 3 == 4
print(otros)

#Práctica Operadores Lógicos 3
#Verifica si las palabras almacenadas en las siguientes variables:
#palabra1 = éxito, y
#palabra2 = tecnología"
#no se encuentran en la frase a continuación, y almacena el resultado de esta comprobación (un booleano) en una variable llamada mi_bool:
#Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
#Elon Musk
frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"
mi_bool = not (palabra1 in frase and palabra2 in frase) 