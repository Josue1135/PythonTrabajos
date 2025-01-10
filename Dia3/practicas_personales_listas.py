'''
Ejercicio con Listas:
    Crea un programa que gestione una lista de compras.
    El programa debe permitir:
    Añadir productos a la lista
    Eliminar productos de la lista
    Mostrar la lista actual de productos
    Verificar si un producto específico está en la lista
    Contar cuántos productos únicos hay en la lista
'''
print("BIENVENIDIO A TU CARRITO DE PRODUCTOS")

productos_lista = []
cantidad_productos = int(input("Ingrese la cantidad de productos para la lista: "))
if cantidad_productos > 0:
    for _ in range(cantidad_productos):
        producto = input("Ingrese un producto para la lista: ")
        productos_lista.append(producto)
print(f"tus productos son: {productos_lista} ")

print("TE EQUIVOCASTE EN TU PRODUCTO, ELIMINALO")
producto_elimar = input("Ingrese un producto para eliminar de tu lista: ")
if producto_elimar in productos_lista:
    print("El producto esta en la lista: ", producto_elimar)
    productos_lista.remove(producto_elimar)
    print("Eliminaste el producto: ", producto_elimar)
else:
    print("El producto no esta en la lista: ", producto_elimar)

print("Tus productos ahora son: ", productos_lista)
total_productos = len(productos_lista)
print(f"En tu lista hay en total {total_productos} productos comprados.")

