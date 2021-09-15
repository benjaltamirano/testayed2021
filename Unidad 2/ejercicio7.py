"""
El programa debe:
- pedir dos datos por consola
- verificar que los dos datos sean numeros enteros
- en caso verdadero imprimir la suma de ambos
- en caso contrario imprimir error
"""
try:
    dato1=int(input("ingrese dato"))
    dato2=int(input("ingrese dato"))
    suma=dato1+dato2
    print(suma)
except:
    print("ingresaste mal los datos salame")
