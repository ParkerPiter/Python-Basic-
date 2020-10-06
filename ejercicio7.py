"""Ejercicio 7"""

print("Contador de días")

mes = int(input("Ingrese número del mes: "))
dia = int(input("Ingrese día: "))

if ( mes == 1 ):
    print("Han pasado: ", dia, "días")
elif ( mes == 2):
    este = dia + 28
    print("Han pasado: ", este, "días")
elif ( mes == 3):
    este = dia + 31 + 28
    print("Han pasado: ", este, "días")
elif ( mes == 4):
    este = dia + 31 + 28 + 31
    print("Han pasado: ", este, "días")
elif ( mes == 5):
    este = dia + 31 + 28 + 31 + 30
    print("Han pasado: ", este, "días")
elif ( mes == 6):
    este = dia + 31 + 28 + 31 + 30 + 31
    print("Han pasado: ", este, "días")
elif ( mes == 7):
    este = dia + 31 + 28 + 31 + 30 + 31 + 30
    print("Han pasado: ", este, "días")
elif ( mes == 8):
    este = dia + 31 + 28 + 31 + 30 + 31 + 30 + 31
    print("Han pasado: ", este, "días")
elif ( mes == 9):
    este = dia + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31
    print("Han pasado: ", este, "días")
elif ( mes == 10):
    este = dia + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30
    print("Han pasado: ", este, "días")
elif ( mes == 11):
    este = dia + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
    print("Han pasado: ", este, "días")
elif ( mes == 12):
    este = dia + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
    print("Han pasado: ", este, "días")
