"""Ejercio 6"""

print("Escriba su peso acontinuación")

libras=int(input("Escriba su peso en libras: "))
cm=float(input("Escriba su estatura en cm: "))

m = cm / 100 
kg = libras * 0.453

imc = kg // m

if ( imc <= 16 ):
    print("Criterio de ingreso...")

elif ( 16 <= 16.9 ):
    print("Infrapeso...")
    
elif ( 17 <= 18.4 ):
    print("Bajo peso...")
    
elif ( 18.5 <= 24.9 ):
    print("Peso normal...")
    
elif ( 25 <= 29.9 ):
    print("Sobrepeso...")
    
elif ( 30 <= 34.9 ):
    print("Obesidad premórbida...")
    
elif ( 40 <= 45 ):
    print("Obesidad mórbida...")
    
elif ( 45 >= 50 ):
    print("Obesidad hipermórbida...")
