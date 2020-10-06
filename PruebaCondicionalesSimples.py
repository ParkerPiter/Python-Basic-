"""Prueba"""

print("Sistema para calcular el promedio de un alumno.")

nombre = input("Para comenzar introduce tú nombre: ")

matematica = int(input(nombre + " Cual es tú calificación en matematica?: "))
fisica = int(input(nombre + " Cual es tú calificación en fisica?: "))
quimica = int(input(nombre + " Cual es tú calificación en quimica?: "))

promedio = (matematica + fisica + quimica) // 3

if promedio >= 6:
    print('Felicidades ' + nombre + ' "Aprobaste" con un promedio de: ', promedio)

print("Fin.")
