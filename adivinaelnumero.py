from random import *

# entrada
numero_ingresado = int(input("ingrese un numero del 1 al 10: "))
# proceso 

numero_generado = randint(1, 10)

if numero_ingresado == numero_generado:
    print("felicidades,adivinaste el numero")
elif numero_ingresado < numero_generado:
    print("el numero a adivinar es mayor a", str(numero_ingresado), "era el" , str(numero_generado))
else:
    print("el numero a adivinar es menor a", str(numero_ingresado), "era el", str(numero_generado))