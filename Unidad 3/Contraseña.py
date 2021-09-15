try:
    contraseña="messi10"
    usuario=(input("Ingrese contraseña: "))
    if usuario == contraseña.lower():
        print("la contraseña es correcta")
    else:
        print("la contraseña es incorrecta")
    
except:
    print("error")
