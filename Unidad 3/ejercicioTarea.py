"""
El programa siguiente muestra el color obtenido al mezclar dos colores en la pantalla, siendo los 3 posibles:
Azul
Rojo
Verde
"""
try:
    primer=input("Ingrese un color:")
    if primer == "rojo":
        segundo=input("Ingrese otro color")
        if segundo == "azul":
            print("morado")
        elif segundo == "verde":
            print("amarillo")
    if primer == "azul":
        segundo=input("ingrese otro color")
        if segundo == "verde":
            print("cyan")
        elif segundo == "rojo":
            print("morado")
    else:
        print("Elije un color valido")
except:
    print("Ingrese un color valido por favor")
