import funciones as fn

while True:
    condicion=input("""Por favor ingrese una opcion
        - 1.suma
        - 2.resta
        - 3.multiplicacion
        - 4.division
        - 5.salir
        ingreso : """)
    if condicion == "1":
        a,b = fn.pedir_numeros()
        print(f"la suma de {a}+{b} = {fn.sumador(a,b)}")
    elif (condicion == "2"):
        a,b = fn.pedir_numeros()
        print(f"la resta de {a}-{b} = {fn.restador(a,b)}")
    elif (condicion == "3:"):
        a,b= fn.pedir_numeros()
        print(f"la multiplicacion de {a}*{b} = {fn.multiplicador(a,b)}")

    elif (condicion == "4:"):
        a,b= fn.pedir_numeros()
        print(f"la division de {a}/{b} = {fn.divisor(a,b)}")

    elif (condicion == "5:"):
        print("Gracias por usar la Calculadora")
        
    else:
        print("error, ninguna opcion es correcta")
    