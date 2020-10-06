"""Ejercicio"""
print("Capicua: ")

aja = int(input("Introduzca un número de 5 dijitos: "))


num1 = aja // 1000

segun = aja % 10 * 10

aja = aja //10

segun = segun + aja % 10

if num1 == segun:
    print ("Funciono")

else:
    print ("No funciono")
