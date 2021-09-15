"""
###**Ejercicio 4.2 (Mediciones)**
El programa debe:
*   Contar con 4 funciones (calcular Area (cuadrado), calcular Perimetro(cuadrado),
    calcular Area (circulo), calcular Perimetro(circulo))
*   Contar con un menu donde debe pedir al usuario que operacion realizar
*   Pedir los dos parametros y devolver el resultado al usuario
*   Gestionar posibles errores

"""
import math as mt

def perimetro_circulo():
    while True:
        try:
            radio=float(input("Ingrese valor del radio"))
            if radio<=0:
                print("El radio debe ser mayor a 0")
            else:
                break
        except:
            print("Error uachin")
    
    return round(2*mt.pi*radio,0),radio

perimetro,radio = perimetro_circulo()
print(f"El radio del circulo es{radio}cm y el perimetro {perimetro}cm")


def area_circulo():
    while True:
        try:
            radio=float(input("Ingrese valor del radio"))
            if radio <=0:
                print("El radio debe ser mayor a cero")
            else:
                break
        except:
            print("error uachin")
    
    return round(mt.pi*radio*radio,0),radio

area, radio = area_circulo()
print(f"El radio de un circulo es {radio}cm y el area es {area}cm cuadrados")

import math as mt
 
def area_cuadrado():
    while True:
        try:
            lado=float(input("Ingrese el lado del cuadrado: "))
            if lado<=0:
                print("El lado de un cuadrado no puede ser negativo, reitentar.")
            else:
                break
        except:
            print("Dato erroeo. Reintentar")

print(f"El area del cuadrado es: {lado*lado}")


def perimetro_cuadrado():
    while True:
        try:
            lado_cuadrado= float(input("Ingrese cuanto mide un lado del cuadrado: "))
            if (lado_cuadrado <= 0):
                print("Ingrese un numero mayor o distinto de cero")
            else:
                 break 
        except:
            print("ERROR. Datos erroneos")

    return lado_cuadrado*4 

while True:
    condicion=input("""Por favor ingrese una opcion:
        1. Calcular area cuadrado
        2. Calcular perimetro cuadrado
        3. Calcular area circulo
        4. Calcular perimetro circulo
        5. Salir
        """)
    if condicion=="1":
        area_cuadrado()
    elif condicion=="2":
        print(f"El perimetro del cuadrado es: {perimetro_cuadrado()}")
    elif condicion=="3":
        area,radio=area_circulo()
        print(f"El radio del circulo es {radio} y el area {area}")
    elif condicion=="4":
        perimetro,radio=perimetro_circulo()
        print(f"El radio del circulo es {radio} y el perimetro {perimetro}")
    elif condicion=="5":
        break
    else:
        print("No ha seleccionado una opción correcta.")


        
