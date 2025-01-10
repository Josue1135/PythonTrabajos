porcentaje = 13 / 100
nombre = input("Ingresa tu nombre: ")
venta = input("Ingrese su venta del mes: ")
comision = int(venta) * porcentaje
print("Su comision del mes es: " + str(comision))
sueldo_total = int(venta) + comision
print(f" Estimado {nombre} tu sueldo total de este mes es: " + str(sueldo_total))


#Modo del docente
print("--------------------------------------------------------")
nombre = input("Ingresa tu nombre: ")
venta = input("Ingrese su venta del mes: ")

venta = int(venta)
comision = venta * 13 / 100
comision = round(comision)

print(f"Su comision del mes es: {comision}")
