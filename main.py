# Diccionario principal donde se almacenarán los estudiantes
estudiantes = {}


# Registra un nuevo estudiante en el sistema.
    
def registrar_ingreso():
   

    nombre = input("Ingrese el nombre del estudiante: ")

    if nombre in estudiantes:
        print("El estudiante ya se encuentra registrado.")
    else:
        estudiantes[nombre] = []
        print(f"Estudiante {nombre} registrado correctamente.")

# Registra una nota a un estudiante existente.
    
def registrar_nota():
   

    nombre = input("Ingrese el nombre del estudiante: ")

    if nombre in estudiantes:

        try:
            nota = float(input("Ingrese la nota: "))

            if 0 <= nota <= 5:
                estudiantes[nombre].append(nota)
                print("Nota registrada correctamente.")
            else:
                print("La nota debe estar entre 0 y 5.")

        except ValueError:
            print("Debe ingresar un número válido.")

    else:
        print("El estudiante no está registrado.")


# Calcula y muestra el promedio de un estudiante.

def ver_promedio():
    
    nombre = input("Ingrese el nombre del estudiante: ")

    if nombre in estudiantes:

        notas = estudiantes[nombre]

        if len(notas) > 0:

            promedio = sum(notas) / len(notas)

            print(f"\nEstudiante: {nombre}")
            print(f"Notas: {notas}")
            print(f"Promedio: {promedio:.2f}")

        else:
            print("El estudiante todavía no tiene notas.")

    else:
        print("El estudiante no está registrado.")
