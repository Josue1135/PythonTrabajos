from time import process_time_ns

texto = input("Ingresa una texto: ")

letras = []

texto = texto.lower()

letras.append(input("Ingresa la primera letra: ").lower())
letras.append(input("Ingresa la segunda letra: ").lower())
letras.append(input("Ingresa la tercera letra: ").lower())

print("\n")

print("Cantidad de letras: ")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetida: {cantidad_letras1} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida: {cantidad_letras2} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida: {cantidad_letras3} veces")
print("\n")

print("Cantidad de palabras en el texto: ")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en el texto")
print("\n")

print("Letras de incio y fin: ")
letra_inicio = texto[0]
letra_fin = texto[-1]
print(f"La letra de inicio es: '{letra_inicio.upper()}' y la final es: '{letra_fin.upper()}'")

print("Texto invertido")
texto_invertido = texto[::-1]
print(f"Texto invertido: '{texto_invertido}'")

print("Buscando la palabra Python")
buscar_python = 'python' in texto
dic = {True:"Si", False:"no"}
print(f"La palabra Python {dic[buscar_python].upper()} se ha encontrado en el texto")

