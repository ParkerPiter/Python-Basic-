"""Prueba"""

print("Sistema para calcular el promedio de un alumno")

nombre = input("Para comenzar, cual es tú nombre?:")

matematica = float(input(nombre + " Cual es tú calificación en matematicas?: "))
quimica = float(input(nombre + " Cual es tú calificación en quimica?: "))
fisica = float(input(nombre + " Cual es tú calificación en fisica?: "))

promedio = (matematica + quimica + fisica) / 3

if promedio >=6:
                print('Felicidades ' + nombre + ' "Aprobaste" con un promedio de: ', promedio)
                print('Felicidades ' + nombre + ' "Aprobaste" con un promedio de: ', round(promedio,2))

else:
    print("Lo sentimos " + nombre + " has 'aplazado' con un promedio de : ", promedio)
    print("Lo sentimos " + nombre + " has 'aplazado' con un promedio de : ", round(promedio,1))

print("Fin. ")
