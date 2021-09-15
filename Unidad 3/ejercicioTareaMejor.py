try:
    primer=input("Ingrese un color: ")
    if primer.lower():
        if primer == "rojo":
            segundo=input("Ingrese otro color: ")
            if segundo == "azul":
                print("morado")
            elif segundo == "verde":
                print("amarillo")
    if primer.lower():
        if primer == "azul":
            segundo=input("ingrese otro color")
            if segundo == "verde":
             print("cyan")
            elif segundo == "rojo":
             print("morado")
    else:
        print("Escribi tu color en minuscula")
except:
    print("Error")
    
