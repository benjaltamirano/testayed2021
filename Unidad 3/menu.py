"""
El programa debe:

Mostrar al usuario un menu
Permitir al usuario ingresar una opcion del menu
imprimir esa opcion
en caso de no escribir ninuna opcion del menu indicar ERROR
Condiciones:

imprimir (string)
1 (int)
2 (int)
salir (string)
Ayuda (como se comparan string y enteros cuidado con castear antes de verificar si el usuario ingreso str o int)
"""
try:
    condicion=input("""Por favor ingrese una opcion
    - imprimir
    - 1
    - 2
    - salir
    ingreso : """)
    if condicion.isalpha():
        if condicion == "imprimir":
            print("ingresaste imprimir")
        elif condicion == "salir":
            print("ingresaste salir")
        else:
            print("no ingresaste una opcion alfabetica correcta")
    elif condicion.isdigit():
        if int(condicion) == 1:
            print("ingresaste menu 1")
        elif int(condicion) == 2:
            print("ingresaste menu 2")
        else:
            print("no ingresaste un numero correctamente")
    else:
        print("no ingresaste numeros y letras")
except:
    print("Por favor escriba una opcion nuevamente")