"""
###**Ejercicio**
El programa debe:
*   Pedir al usuario una palabra
*   Verificar que sea una palabra y no un numero
*   Mostrar por pantalla las letras una a una
*   No producir errores
"""
while True:
    try:
        palabra= str(input("Ingrese una palabra: "))
        if palabra.isalpha():
            for i in palabra:
                print(i,end="")
        else:
            print("Ingresa un numero porfa")
        
        break
    except:
        print("Error")
