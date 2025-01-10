'''
    Ejercicio con Diccionarios:
    Desarrolla un sistema de gestión de estudiantes de una clase. Debes:


    Crear un diccionario donde las claves sean nombres de estudiantes y los valores sean sus calificaciones
    Implementar funciones para:

    Añadir un nuevo estudiante con su calificación
    Actualizar la calificación de un estudiante existente
    Calcular el promedio de calificaciones de la clase
    Encontrar el estudiante con la calificación más alta
'''

alumnos = {}
def registrar_alumno(alumnos):
    nombre = input("Ingresa el nombre del alumnos: ").strip()
    if nombre in alumnos:
        print(f"El alumno {nombre} ya existe. Ingresale su nota")
        return
    try:
        nota = float(input(f"Ingresa la nota de {nombre}: "))
        if 0 <= nota <= 20:
            alumnos[nombre] = nota
            print(f"Alumno {nombre} creado correctamente con su {nota}.")
        else:
            print("La nota debe ser entre 0 y 20")
    except ValueError:
        print("Ingrese una nota valida")



#menu
while True:
    registrar_alumno(alumnos)