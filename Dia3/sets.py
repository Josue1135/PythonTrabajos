mi_set = set((1,2,3,4,5))
print(mi_set)
print(type(mi_set))

print("--------\n")
#print(mi_set[10])
print(1 in mi_set)

print("--------\n")
print(len(mi_set))

print("-----UNIR SET---\n")
s1 = {1,2,3}
s2 = {4,5,6}
s3 = s1.union(s2)
print(s3)


print("----AGREGAR----\n")
s4 = {1,2,3}
print(s4)
s4.add(4)
print(s4)


print("----ELIMINAR----\n")
S5 = {1,2,3,4,5,6}
S5.remove(4)
print(S5)


print("----DESCARTE----\n")
s6 = {1,2,3,4,5,6}
s6.discard(4)
print(s6)


print("----POP . VACIO ----\n")
s7 = {1,2,3,4,5,6}
sorteo = s7.pop()
print(sorteo)


print("---LIMPIAR . VACIO-----\n")
s8 = {1,2,3,4,5,6}
s8.clear()
print(s8)

#Une los siguientes sets en uno solo, llamado mi_set_3:
#{1, 2, "tres", "cuatro"}
#{"tres", 4, 5}

mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}
mi_set_3 = mi_set_1.union(mi_set_2)
print(mi_set_3)

#Elimina un elemento al azar del siguiente set, utilizando métodos de sets.

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.pop()
print(sorteo)

#Agrega el nombre Damián al siguiente set, utilizando métodos de sets:
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add("Damián")
print(sorteo)

