import csv

# Cargos
CARGOS = ['CEO', 'Desarrollador', 'Analista de datos'];
# Lista para almacenar los trabajadores
trabajadores = []

# Opción 1 - Registrar trabajadores
def registrar_trabajador():
    while True:
        nombre = input("Ingrese nombre y apellido del trabajador: ");
        cargo = input("Ingrese el cargo del trabajador (CEO, Desarrollador, Analista de datos): ");
        while cargo not in CARGOS:
            print("Cargo ingresado no válido. (CEO, Desarrollador, Analista de datos)");
            cargo = input("Ingrese el cargo del trabajador (CEO, Desarrollador, Analista de datos): ");
        sueldo_bruto = float(input("Ingrese el sueldo bruto del trabajador: "));
        
        # Calculando descuentos
        descuento_salud = sueldo_bruto * 0.07
        round(descuento_salud);
        descuento_afp = sueldo_bruto * 0.12
        round(descuento_afp);
        sueldo_liquido = sueldo_bruto - (descuento_salud + descuento_afp)
        
        trabajador = {
            "Nombre": nombre,
            "Cargo": cargo,
            "Sueldo Bruto": sueldo_bruto,
            "Descuento Salud": descuento_salud,
            "Descuento AFP": descuento_afp,
            "Sueldo Líquido": sueldo_liquido 
        }

        trabajadores.append(trabajador);
        

        print(f"Trabajador {nombre} registrado correctamente.\n")

        try:
            repetir = int(input("¿Desea agregar otro trabajador?\n1. Si\n2. No\n> "))
        except ValueError:
            print("Ingrese una respuesta válida.")
        if repetir == 1:
            print('')
        elif repetir == 2: 
            break
        

    

# opción 2 - listar trabajadores
def listar_trabajadores():
    if not trabajadores:
        print("No hay trabajadores registrados.")
        return
    
    print("------- Lista de trabajadores -------\n");
    for diccionario in trabajadores:
        print(diccionario, sep='')



# Opción 3 - planilla ha imprimir
def imprimirplantilla():
    while True:
        print("""*** Imprimir plantilla de sueldos ***
1) Todos los cargos
2) Cargo CEO
3) Cargo Desarrollador
4) Cargo Analista de datos
5) Volver al menú
        """)
        
        opcion = input("Ingrese el número de opción deseada: ")
        
        if opcion == '1':
            with open("plantilla_sueldo.txt", "w", encoding="utf-8") as archivo:
                archivo.write("Trabajador - Cargo - Sueldo - Desc. Salud - Desc. AFP - Líquido a pagar\n")
                for trabajador in trabajadores:
                    archivo.write(f"{trabajador['Nombre']} - {trabajador['Cargo']} - {trabajador['Sueldo Bruto']} - {trabajador['Descuento Salud']} - {trabajador['Descuento AFP']} - {trabajador['Sueldo Líquido']}\n\n")
                print("Plantilla impresa en 'plantilla_sueldo.txt'.\n")
        
        elif opcion == '2':
            with open("plantilla_sueldo.txt", "w", encoding="utf-8") as archivo:
                archivo.write("Trabajador - Cargo - Sueldo - Desc. Salud - Desc. AFP - Líquido a pagar\n")
                for trabajador in trabajadores:
                    if trabajador['Cargo'] == 'CEO':
                        archivo.write(f"{trabajador['Nombre']} - {trabajador['Cargo']} - {trabajador['Sueldo Bruto']} - {trabajador['Descuento Salud']} - {trabajador['Descuento AFP']} - {trabajador['Sueldo Líquido']}\n")
                print("Plantilla para el cargo CEO impresa en 'plantilla_sueldo.txt'.\n")
        
        elif opcion == '3':
            with open("plantilla_sueldo.txt", "w", encoding="utf-8") as archivo:
                archivo.write("Trabajador - Cargo - Sueldo - Desc. Salud - Desc. AFP - Líquido a pagar\n")
                for trabajador in trabajadores:
                    if trabajador['Cargo'] == 'Desarrollador':
                        archivo.write(f"{trabajador['Nombre']} - {trabajador['Cargo']} - {trabajador['Sueldo Bruto']} - {trabajador['Descuento Salud']} - {trabajador['Descuento AFP']} - {trabajador['Sueldo Líquido']}\n")
                print("Plantilla para el cargo Desarrollador impresa en 'plantilla_sueldo.txt'.\n")
        
        elif opcion == '4':
            with open("plantilla_sueldo.txt", "w", encoding="utf-8") as archivo:
                archivo.write("Trabajador - Cargo - Sueldo - Desc. Salud - Desc. AFP - Líquido a pagar\n")
                for trabajador in trabajadores:
                    if trabajador['Cargo'] == 'Analista de datos':
                        archivo.write(f"{trabajador['Nombre']} - {trabajador['Cargo']} - {trabajador['Sueldo Bruto']} - {trabajador['Descuento Salud']} - {trabajador['Descuento AFP']} - {trabajador['Sueldo Líquido']}\n")
                print("Plantilla para el cargo Analista de datos impresa en 'plantilla_sueldo.txt'.\n")
        
        elif opcion == '5':
            break
        
        else:
            print("Ingrese una opción válida.\n")          