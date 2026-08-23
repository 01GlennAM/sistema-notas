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

