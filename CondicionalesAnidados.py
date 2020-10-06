print("=========")
print("Conversor")
print("========= \n")

print("Menú de opciones: \n")
print("Presiona 1 para convertir de número a palabra.")
print("Preciona 2 para convertir de palabra a número. \n")

opcion = int(input("Cual es tu opcion deseada?: "))

if opcion == 1:
    print("\n Conversor de número a palabra. \n")

    opcion_uno = int(input("Cual es el número que deas convertir?: "))

    if opcion_uno == 1:
        print("El número es 'Uno'")
    elif opcion_uno == 2:
        print("El número es 'Dos'")
    elif opcion_uno == 3:
        print("El número es 'Tres'")
    elif opcion_uno == 4:
        print("El número es 'Cuatro'")
    elif opcion_uno == 5:
        print("El número es 'Cinco'")
    else:
        print("El número seleccionado no esta registrado")

elif opcion == 2:
    print("\n Conversor de palabra a Número. \n")

    opcion_dos = input("Cual es la palabra que deseas convertir?: ")

    if opcion_dos == "uno":
        print("el número es '1'")
    elif opcion_dos == "dos":
        print("El número es el '2'")
    elif opcion_dos == "tres":
        print("El número es el '3'")
    elif opcion_dos == "cuatro":
        print("El número es el '4'")
    elif opcion_dos == "cinco":
        print("El número es el '5'")
    else:
        print("El numero seleccionado no esta registrado")

else:
    print("Opción no disponible")

print("Fin.")
