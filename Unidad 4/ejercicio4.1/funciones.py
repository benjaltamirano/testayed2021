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