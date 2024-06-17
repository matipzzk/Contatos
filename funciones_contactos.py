import os
import csv
import time

contactos = []

def opcion_1():
    os.system('cls')
    nombre = input("Ingrese nombre del contacto: ")
    if len(nombre) < 3 or not nombre.isalpha():
        print("Nombre no válido. Debe tener al menos 3 letras y no contener números.")
        return
    while True:
        try:
            nro = int(input("Ingrese télefono del contacto: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")
    correo = input("Ingrese correo eléctronico del contacto: ")
    if "@" not in correo:
        print("Correo no válido")
        return

    contacto = {
        "nombre": nombre,
        "número": nro,
        "correo": correo
    }
    contactos.append(contacto)

def opcion_2():
    os.system('cls')
    if not contactos:
        print("No hay contactos para mostrar.")
    else:
        print("LISTA DE CONTACTOS")
        for x in contactos:
            print(f"Nombre: {x['nombre']} - Número: {x['número']} - Correo: {x['correo']}")

def opcion_3():
    os.system('cls')
    with open('contactos.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["nombre", "número", "correo"])
        writer.writeheader()
        for contacto in contactos:
            writer.writerow({"nombre": contacto["nombre"], "número": str(contacto["número"]), "correo": contacto["correo"]})
    print("Contactos guardados en 'contactos.csv'.")

def opcion_4():
    os.system('cls')
    print("Hasta luego...")
    time.sleep(2)
    return False
