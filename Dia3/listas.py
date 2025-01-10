mi_lista = ["a", "b", "c", "d", "e"]
print(mi_lista)
print(type(mi_lista))
print("....................................")
otra_lista =["1" , 1.2, 5, -1, True, "nombres"]
print(otra_lista)
resultado = mi_lista[0:2]
print(resultado)
print(len(otra_lista))
print("........................................")
print("concatenacion de listas")
print(mi_lista + otra_lista)
lista3 = mi_lista + otra_lista
print(lista3)
print("..........................................")
lista3[2] = "cambiado"
print(lista3)
lista3.append('agregado otra vez')
print(lista3)
print(".....................................")
eliminado = lista3.pop(0)
print(eliminado)
print(lista3)
print("........................................")
lista4 = ['g', 'p', 'j', 'r', 'q', 'a']
lista4.sort() # para ordenar los elementos
print(lista4)
print("........................................")
lista4.reverse()
print(lista4)

print("######### EJERCICIOS ######################")
#Crea una lista con 5 elementos, dentro de la variable mi_lista. Puedes incluir strings, booleanos, números, etc.
mi_lista = ['h', 'a', 2, 2.5 , False]
print(mi_lista)

#Agrega el elemento "motocicleta" a la siguiente lista de medios de transporte:
#medios_transporte = ["avión", "auto", "barco", "bicicleta"]
#No debes modificar la línea de código ya suministrada, sino que debes emplear el método apropiado de listas para añadir un nuevo elemento.

medios_transporte = ["avión", "auto", "barco", "bicicleta"]
print(medios_transporte)
medios_transporte.append('motocicleta')
print(medios_transporte)

#Utiliza el método pop() para quitar el tercer elemento
# de la siguiente lista llamada frutas, y almacénalo
# en una variable llamada eliminado. Utiliza métodos de
# listas sin alterar la línea de código ya suministrada.

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)
print(eliminado)
print(frutas)



