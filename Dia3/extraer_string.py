#rebanar -> slicing

texto = "ABCDEFGHIJKLMOPQRSTUVWXYZ"
fragmento = texto[2]
print(fragmento)

#fragmento = texto[5 (posicion),
# 5 ([2:5] los caracteres que quieren obtener entre esos Índices),
# 2 (de cuanto es cuantos quieres obtener)[

fragmento = texto[2:5]
print(fragmento)

#omitir el 2 fac te imprime los restantes
fragmento = texto[2:]
print(fragmento)

#De cuantos en cuanto imprimo (Último nÚmero)
fragmento = texto[2:14:2]
print(fragmento)

#imprime al revez desde el final
fragmento = texto[::-1]
print(fragmento)

#Práctica Sub-Strings 1
#Extrae la primera palabra de la siguiente frase utilizando slicing, y muéstrala en pantalla:
#"Controlar la complejidad es la esencia de la programación"
#Pista: "Controlar" tiene un largo de 9 caracteres.

frase = "Controlar la complejidad es la esencia de la programación"
fragmento = frase[0:9]
print(fragmento)



#Toma cada tercer caracter empezando desde el noveno hasta el final de la frase, e imprime el resultado.
#"Nunca confíes en un ordenador que no puedas lanzar por una ventana"

frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
fragmento = frase[8::3]
print(fragmento)

#Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado en pantalla.
#"Es genial trabajar con ordenadores. No discuten lo recuerdan todo y no se beben tu cerveza"

frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
fragmento = frase[::-1]
print(fragmento)

