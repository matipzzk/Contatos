from funciones_contactos import *



while True:
    print("""
        Menú de opciones
    1. Agregar un contacto
    2. Mostrar contactos
    3. Guardar contactos en un archivo CSV
    4. Salir""")
    try:
        opc = int(input("Ingrese una opción: "))
    except:
        print("Por favor, ingrese un número válido.")
        continue

    if opc == 1:
        opcion_1()
    elif opc == 2:
        opcion_2()
    elif opc == 3:
        opcion_3()
    elif opc == 4:
        if not opcion_4():
            break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")