flag1 = True
while flag1:
    try:
        numero_inicial=int(input("ingrese un numero inicial"))
        numero_limite=int(input("ingrese numero limite"))
    except:
        print("dije un numero salame")

if numero_inicial < numero_limite:
    while numero_inicial <= numero_limite:
        print(numero_inicial)
        numero_inicial+=1
        flag1 = False
else:
    print("el numero inicial debe ser menor al numero limite")

