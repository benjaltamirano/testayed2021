"""
Agencia de autos:

El programa cuenta con tres marcas de autos y su precio.

El programa debe:

pedir al usuario que ingrese la cant de dinero que dispone.
verificar que la cantidad ingresada sea un numero y sino mostrar error
verificar la cantidad de ingresada e indicar que auto o autos puede comprar
Ford = 10000
Renault = 11000
Chevrolet = 15000
"""
try:
    dinero=float(input("ingresar dinero que tenes"))
    if dinero >=10000:
        print("podes comprarte un ford traqui")
    if dinero >=11000:
        print("podes comprarte un renaut o chevrolet")

except:
    print("error")


