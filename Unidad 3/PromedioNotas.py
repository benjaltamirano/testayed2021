try:
    dato1= float(input("ingrese un dato 1"))
    dato2= float(input("ingrese un dato 2"))
    dato3= float(input("ingrese un dato 3"))
    promedio= round ((dato1+dato2+dato3)/3,2)
    print(f"el promedio de los numeros es:{promedio} ")

except:
    print("alguna nota esta mal ingresada")
