"""
###**Ejercicio 4.1 (Calculadora)**
El programa debe:
*   Contar con 4 funciones (suma, resta, división y multiplicación)
*   Contar con un menu donde debe pedir al usuario que operacion realizar
*   Pedir los dos numero para operar y devolver el resultado al usuario
*   Gestionar posibles errores
"""

def sumador(a,b):
    suma=float(a)+float(b)
    return suma

def restador(a,b):
    resta=float(a)-float(b)
    return resta

def divisor(a,b):
    try:
        division=round(float(a)/float(b),2)
    except:
        print("la division genero error")
        division= "error"
    
    return division

def multiplicador(a,b):
    multiplicacion=float(a)*float(b)
    return multiplicacion

def pedir_numeros():
    while True:
        try:
            num1= float(input("1 argumento"))
            num2= float(input("2 argumento"))
            break
        except:
            print("argumentos incorrectos")

    return num1,num2

while True:
    
    condicion=input("""Por favor ingrese una opcion
        - 1.suma
        - 2.resta
        - 3.multiplicacion
        - 4.division
        - 5.salir
        ingreso : """)
    if condicion == "1":
        a,b = pedir_numeros()
        print(f"la suma de {a}+{b} = {sumador(a,b)}")
    elif (condicion == "2"):
        a,b = pedir_numeros()
        print(f"la resta de {a}-{b} = {restador(a,b)}")
    elif (condicion == "3:"):
        a,b= pedir_numeros()
        print(f"la multiplicacion de {a}*{b} = {multiplicador(a,b)}")

    elif (condicion == "4:"):
        a,b= pedir_numeros()
        print(f"la division de {a}/{b} = {divisor(a,b)}")

    elif (condicion == "5:"):
        print("Gracias por usar la Calculadora")
        
    else:
        print("error, ninguna opcion es correcta")
    
    
        




    