Datos = {
    "Alumnos": [
        {
            "Nombre": "Julia",
            "Apellido": "Alfajores",
            "DNI": "1234567",
            "Fecha de nacimiento": "29/04/2007",
            "Tutor": "Abuela",
            "Notas": [8,10,6],
            "Faltas": 0,
            "Amonestaciones": 0
        }
    ]
}

def agregar_alumno():
    alumno = {}
    alumno["Nombre"] = input("Nombre del alumno: ")
    alumno["Apellido"] = input("Apellido del alumno: ")
    alumno["DNI"] = input("DNI del alumno: ")
    alumno["Fecha de nacimiento"] = input("Fecha de nacimiento (dd/mm/aaaa): ")
    alumno["Tutor"] = input("Nombre del tutor: ")
    alumno["Notas"] = []
    alumno["Faltas"] = 0
    alumno["Amonestaciones"] = 0

    Datos["Alumnos"].append(alumno)
    print("Alumno agregado correctamente.")

def mostrar_alumnos():
    if not Datos["Alumnos"]:
        print("No hay alumnos registrados.")
        return

    for i, alumno in enumerate(Datos["Alumnos"]):
        print(f"\nAlumno {i+1}:")
        for clave, valor in alumno.items():
            print(f"{clave}: {valor}")

def modificar_alumno():
    mostrar_alumnos()
    if not Datos["Alumnos"]:
        return

    indice = int(input("Número de alumno a modificar (1, 2, 3...): ")) - 1

    if 0 <= indice < len(Datos["Alumnos"]):
        alumno = Datos["Alumnos"][indice]
        print("Datos actuales del alumno:")
        for clave, valor in alumno.items():
            print(f"{clave}: {valor}")

        campo = input("¿Qué campo deseas modificar? (Nombre, Apellido, DNI, Fecha de nacimiento, Tutor, Faltas, Amonestaciones): ")
        if campo in alumno and campo not in ["Notas"]:
            nuevo_valor = input(f"Ingresar nuevo valor para {campo}: ")
            if campo in ["Faltas", "Amonestaciones"]:
                nuevo_valor = int(nuevo_valor)
            alumno[campo] = nuevo_valor
            print("ato modificado.")
        else:
            print("Campo inválido o no se puede modificar directamente.")
    else:
        print("Número de alumno inválido.")


def agregar_nota():
    mostrar_alumnos()
    if not Datos["Alumnos"]:
        return

    indice = int(input("Número de alumno al que agregar nota: ")) - 1
    if 0 <= indice < len(Datos["Alumnos"]):
        nota = float(input("Nota a agregar: "))
        Datos["Alumnos"][indice]["Notas"].append(nota)
        print("Nota agregada.")
    else:
        print("Número de alumno inválido.")


def expulsar_alumno():
    mostrar_alumnos()
    if not Datos["Alumnos"]:
        return

    indice = int(input("Número de alumno a expulsar: ")) - 1
    if 0 <= indice < len(Datos["Alumnos"]):
        eliminado = Datos["Alumnos"].pop(indice)
        print(f"Alumno {eliminado['Nombre']} {eliminado['Apellido']} expulsado.")
    else:
        print("Número de alumno inválido.")


def menu():
    while True:
        print("\n *** MENÚ ESCUELA!!!1!! :OOO *** ")
        print("1. Agregar alumno")
        print("2. Mostrar alumnos")
        print("3. Modificar alumno")
        print("4. Agregar nota a alumno")
        print("5. Expulsar alumno")
        print("6. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            agregar_alumno()
        elif opcion == "2":
            mostrar_alumnos()
        elif opcion == "3":
            modificar_alumno()
        elif opcion == "4":
            agregar_nota()
        elif opcion == "5":
            expulsar_alumno()
        elif opcion == "6":
            print("¡Adiós!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

menu()
