"""
El programa debe:
*   mostrar el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
*  si el usuario escribe "hola" o "chau" que no se haga el eco
"""
while True:
    palabra_usuario=(input("ingrese una palabra: "))
    if palabra_usuario == "salir":
        print("Ya fue")
        break
    elif palabra_usuario == "hola" or palabra_usuario== "chau":
        continue
    else:
        print(f"ingresaste {palabra_usuario}")

