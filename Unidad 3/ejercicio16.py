while 1:
    try:
      dato_numerico=int(input("ingrese un numero"))
    except:
        print("error")
multiplicador=1
while multiplicador<=10:
    print(f"{multiplicador} x {dato_numerico} = {multiplicador * dato_numerico}" )
    multiplicador+=1
