""" Simular un cajero automatico y pedir usuario y contraseña (user, 1234) caso verdadero mostrar menu y en caso falso seguir pidiendo."""

condicion=fa.validar_usuario()

def validar_usuario():
    for i in range(3):
        usuario=(input("Ingrese el usuario: "))
        contraseña=(input("Ingrese contraseña: "))
        if usuario=="user" and contraseña == "1234":
            return True
        else:
            print(f"Quedan {2-i} intentos")
    return False