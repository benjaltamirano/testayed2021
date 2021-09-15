"""
El programa debe:
- pedir en orden el Nombre, apellido, edad y numero de calzado
- verificar que cada uno sea el tipo de variable correcto (IMPORTANTE)
- en caso verdadero imprimir de la siguiente manera el resultado:
"""
try:
    nombre=(input("Ingrese su nombre:"))
    apellido=(input("Ingrese su apellido:"))
    edad=int(input("Ingrese su edad:"))
    calzado=float(input("ingrese su numero de calzado:"))
    print(nombre)
    print(apellido)
    print(edad)
    print(calzado)
except:
    print("Error")
