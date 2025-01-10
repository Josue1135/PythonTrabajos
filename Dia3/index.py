mi_texto = "Esto es una prueba"
resultado = mi_texto[-4]
print(resultado)

#metodo para buscar una palabra
otro_texto = "nueva prueba"
resultado = otro_texto.index("prueba")
print(resultado)

#
resultado = otro_texto.index("a", 2, 11)
print(resultado)

# r index-> busca de derecha a izquierda
resultado = otro_texto.rindex("a")
print(resultado)


#Práctica Método Index() 2
# y muestra en pantalla el índice de la primera aparición de la palabra "práctica" en la siguiente frase:

#"En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado = frase.index("práctica")
print(resultado)

#Práctica Método Index() 3
#Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la siguiente frase:
#"En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado = frase.rindex("práctica")
print(resultado)






