opcion = ""

while opcion != "salir":
    opcion = input("escribe 'Hola' o 'salir': ")
    if opcion == "Hola":
        print("¡Hola, mucho gusto!")
    elif opcion != "salir":
        print("Opción no valida")
        break
print("hasta luego")