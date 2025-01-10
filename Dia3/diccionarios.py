diccionario = {'c1':'valor1', 'c2':'valor2', 'c3':'valor3'}
print(diccionario)
print(type(diccionario))
resultado = diccionario.get('c2')
resultado2 = diccionario['c2']
print(resultado)
print(resultado2)

print("-------------------------------\n")
cliente = {'nombre':'Josue', 'apellido':'Vera', 'peso':70, 'talla':169.9}
consulta = (cliente['peso'])
print(consulta)

print("-------------------------------\n")
dic = {'c1':55, 'c2':[10,20,20], 'c3':{'nombre':'Josue', 'edad':27}}
print(dic['c2'][1])
print(dic['c3']['edad'])

print("-------------------------------\n")
dicc = {'c1':['a', 'b', 'c'], 'c2':['d', 'e', 'f']}
print(dicc['c2'][2].upper())

print("------AGREGAR ELEMENTOS AL DICCIONARIO-----\n")
agregar = {1:'a', 2:'b', 3:'c'}
print(agregar)
agregar[4] = 'e'
print(agregar)
agregar[2] = 'B' #Sobreescribir el elemento b -> B
print(agregar)

print("----OTROS METODOS-------\n")
print(agregar)
print(agregar.keys()) # conoces las claves todas
print(agregar.values()) #trae los valores del diccionario
print(agregar.items()) #todo lo del diccionario

#Práctica Diccionarios 2
#Crea una función print que devuelva del segundo item de la lista llamada points2,
#dentro del siguiente diccionario.
# Si el valor 300 cambiara en el futuro, el código debería funcionar igual para devolver
# el valor que se encuentre en esa misma posición.
#Para ello, deberás hacer referencia a los nombres de las claves y/o índices según corresponda.

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict['puntos']['points2'][1])


#Actualiza la información de nuestro diccionario llamado mi_dic  (reasignando nuevos valores a las claves según corresponda), y agrega una nueva clave llamada "pais" (sin tilde). Los nuevos datos son:
#nombre: Karen
#apellido: Jurgens
#edad: 36
#ocupacion: Editora
#pais: Colombia
#para ello, no debes cambiar la línea de código ya escrita, sino actualizar los valores mediante métodos de diccionarios.

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic["edad"] = 36
mi_dic["ocupacion"] = "Editora"
mi_dic["pais"] = "Colombia"
print(mi_dic)