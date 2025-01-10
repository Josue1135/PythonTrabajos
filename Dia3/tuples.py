mi_tuple = (1,2,3,4)

print(type(mi_tuple))

tuple_simple = (1, 'a', 1.1, True)
print(tuple_simple)
print(tuple_simple[0])
print(tuple_simple[1])

print("----TUPLE DENTRO DEL TUPLE---")
otra_tuple_simple = (1, 'a', 1.1, ('otra', 'tupla', 2), True)
otra_tuple_simple = list(otra_tuple_simple)
print(otra_tuple_simple)
print(type(otra_tuple_simple))
print("---- TUPLE---")
t = (1, 2, 3)
x,y,z = t
print(t)
print(type(t))

print("---- TUPLE---")
t = (1, 2, 3, 4)
print(len(t))
print(t.count(3)) #contar el valor las veces que aparece en el tuple
print(t.index(1)) #en que posicion se encuentra el elemento imprimido


#Utiliza un método de tuplas para contar la cantidad de veces que aparece el
# valor 2 en la siguiente tupla, y muestra el resultado (integer) en pantalla:

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
cont = mi_tupla.count(2)
print(cont)
print(type(cont))

#Convierte a lista la siguiente tupla, y almacénala en una variable llamada mi_lista.
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)
print(mi_lista)

#Extrae los elementos de la siguiente tupla en cuatro variables: a, b, c, d
mi_tupla = (1, 2, 3, 4)
a,b,c,d = mi_tupla
print(mi_tupla)


