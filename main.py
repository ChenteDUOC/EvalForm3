import csv
import func as Funcion




print("--------    BIENVENIDO    --------");
while True:
    try:
        opcion=int(input("¿Qué operación desea realizar?\n1. Registrar trabajadores.\n2. Listar todos los trabajadores.\n3. Imprimir plantilla de sueldos.\n4. Salir del programa.\n> "));

        if opcion==1:
            Funcion.registrar_trabajador()
        elif opcion==2:
            Funcion.listar_trabajadores()
        elif opcion==3:
            Funcion.imprimirplantilla()
        elif opcion==4:
            print("Cerrando programa...")
            break 
        else: print("Ingrese una opción válida.")

    except ValueError:
        print("Respuesta no válida.")
    except NameError:
        print("No se ha encontrado ningun trabajador registrado. Pruebe con registrar trabajador.\n")