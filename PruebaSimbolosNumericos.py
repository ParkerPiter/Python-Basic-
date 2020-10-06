print("Introduce dos números a comparar: \n")

numUno= int(input("Introduce el primer número: "))
numDos = int(input("Introduce el segundo número: "))

print("\n Los números a comparar son: ", numUno, " y ", numDos, "\n")

if numUno == numDos:
    print("Es igual...")
if numUno != numDos:
    print("Es diferente...")
if numUno < numDos:
    print("Es menor...")
if numUno > numDos:
    print("Es mayor...")
if numUno <= numDos:
    print("Es menor o igual...")
if numUno >= numDos:
    print("Es mayor o igual...")
