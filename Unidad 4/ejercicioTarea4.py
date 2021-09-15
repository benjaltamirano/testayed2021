"""
*   Contar con 4 funciones:
  1.  Conversor de Grados Celcius a Fahrenheit(temperatura en °C).(buscar regla)
  2.  Conversor de cm3 a litros (cantidad de cm3)
  3.  Conversor de litros a cm3 (cantidad de litros)
  4.  Pesos a Dolares (pesos)
*   Contar con un menu donde debe pedir al usuario que operacion realizar
*   Pedir los parametros y devolver el resultado al usuario
*   Gestionar posibles errores
"""
def grados_celcius (temperatura):
    celsius=float(input("Ingrese la cantidad de grados celcius a convertir: "))
    fahrenheit= (9/5)*celsius+32
    return fahrenheit

def cm3 (cantidad_cm3):
    centrimetros_cubicos=float(input("Ingrese cantidad de cm3 a convertir: "))
    litros= centrimetros_cubicos/1000
    return litros
    

def litros (cantidad_litros):
    litros=float(input("Ingrese cantidad de litros a convertir: "))
    centimetos3= litros*1000
    return centimetos3

def dolar (pesos):
    pesos=float(input("Ingrese cantidad de pesos a convertir: "))
    dolar=pesos/180
    return dolar
    

while True:
    condicion=input("""Por favor ingrese una opcion
        - 1.Conversor de Grados Celcius a Fahrenheit
        - 2.Conversor de cm3 a litros
        - 3.Conversor de litros a cm3
        - 4.Conversor de pesos a dolar
        - 5.salir
        ingreso : """)
    if condicion == "1":
        print(f"los grados fahrenheit son = {grados_celcius(grados_celcius)}")
    elif condicion == "2":
        print(f"Los litros son = {cm3(cm3)}")
    elif condicion == "3":
        print (f"Los centimetros cubicos son = {litros(litros)}")
    elif condicion == "4":
        print (f"Los dolares son = {dolar(dolar)}")
    elif condicion == "5":
        print ("Gracias por usar el convertidor")
    else:
        print("Ingrese una opcion valida")
        break

    
