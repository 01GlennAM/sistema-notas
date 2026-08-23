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


# Verifica si el estudiante aprobó o reprobó.
def verificar_aprobacion():
    
    nombre = input("Ingrese el nombre del estudiante: ")

    if nombre in estudiantes:

        notas = estudiantes[nombre]

        if len(notas) > 0:

            promedio = sum(notas) / len(notas)

            print(f"\nPromedio de {nombre}: {promedio:.2f}")

            if promedio >= 3.0:
                print("Estado: APROBADO")
            else:
                print("Estado: REPROBADO")

        else:
            print("El estudiante no tiene notas registradas.")

    else:
        print("El estudiante no está registrado.")



