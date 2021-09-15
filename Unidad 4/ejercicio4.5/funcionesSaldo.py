dinero_disponible=50000
"""ingresa dinero al sistema y actualiza el saldo"""
def ingresar_y_actualizar (dinero_disponible):
    while True:
        try:
            dinero_ingresar=float(input("Ingrese dinero a depositar:"))
            
        except:
            print("error en los parametros")
        if dinero_ingresar >0:
            break
        else:
            print("por favor ingrese una suma positiva")

    dinero_disponible+=dinero_ingresar
    return dinero_disponible

def retirar_y_actualizar (dinero_disponible):
    while True:
        try:
            dinero_a_retirar=float(input("Ingrese dinero a retirar: "))
        except:
            print("error")
        if dinero_a_retirar >0:
            break
        else:
            print("Ingrese una suma positiva")
    dinero_disponible-=dinero_a_retirar
    return dinero_disponible

def consultar_saldo (dinero_disponible):
    print(f"El dinero disponible es {dinero_disponible}")

dinero_disponible=50000
dinero_disponible=ingresar_y_actualizar(dinero_disponible)
print(f"El dinero es: {dinero_disponible}")