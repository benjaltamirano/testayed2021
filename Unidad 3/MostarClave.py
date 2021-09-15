"""
###**Ejercicio (Ahora con flag)**
El programa debe:
*  pedir un dato al usuario
*  solo en caso que este escriba la palabra clave "python" imprimir por pantalla "Correcto", en caso contrario debe seguir pidiendo el dato
*  no deben aparecer errores.
"""
flag= True
try:
    while flag:
        usuario=input("ingrese dato:")
        if usuario == "python":
            print("Correcto")
            flag= False
except:
    print("error")